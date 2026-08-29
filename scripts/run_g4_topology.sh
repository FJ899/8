#!/usr/bin/env bash
set -euo pipefail

OUT=${1:-g4-topology-evidence}
rm -rf "$OUT"
mkdir -p "$OUT"
exec 9>"$OUT/commands.trace"
export BASH_XTRACEFD=9
set -x

ROOT=$(pwd)
PRIVATE_ROOT=$(mktemp -d /tmp/agency-kernel-g4-private.XXXXXX)
SOCKET_ROOT=$(mktemp -d /tmp/agency-kernel-g4-ipc.XXXXXX)
REPO="$PRIVATE_ROOT/target.git"
LEDGER="$PRIVATE_ROOT/control.sqlite"
SOCKET="$SOCKET_ROOT/broker.sock"
READY="$SOCKET_ROOT/ready"
CLIENT="$SOCKET_ROOT/g4_client.py"
REF='refs/heads/kernel-test'
REF_EFFECT='REF(refs/heads/kernel-test)'
A_EFFECT='PATH(A.txt)'
B_EFFECT='PATH(B.txt)'

cleanup() {
  if [[ -n "${BROKER_PID:-}" ]] && kill -0 "$BROKER_PID" 2>/dev/null; then
    PYTHONPATH="$ROOT" python scripts/g2_ipc_client.py --socket "$SOCKET" --request '{"action":"shutdown"}' >/dev/null 2>&1 || true
    wait "$BROKER_PID" 2>/dev/null || true
  fi
  sudo userdel -f g4requester 2>/dev/null || true
  sudo userdel -f g4hostile 2>/dev/null || true
  rm -rf "$PRIVATE_ROOT" "$SOCKET_ROOT"
}
trap cleanup EXIT

sudo userdel -f g4requester 2>/dev/null || true
sudo userdel -f g4hostile 2>/dev/null || true
sudo useradd --no-create-home --shell /usr/sbin/nologin g4requester
sudo useradd --no-create-home --shell /usr/sbin/nologin g4hostile
REQUESTER_UID=$(id -u g4requester)
HOSTILE_UID=$(id -u g4hostile)
chmod 700 "$PRIVATE_ROOT"
chmod 777 "$SOCKET_ROOT"
cp "$ROOT/scripts/g2_ipc_client.py" "$CLIENT"
chmod 755 "$CLIENT"

PYTHONPATH="$ROOT" python scripts/g4_broker.py \
  --socket "$SOCKET" --ledger "$LEDGER" --repo "$REPO" \
  --authorized-uid "$REQUESTER_UID" --ready-file "$READY" \
  >"$OUT/broker.stdout" 2>"$OUT/broker.stderr" &
BROKER_PID=$!
for _ in $(seq 1 100); do
  [[ -S "$SOCKET" && -f "$READY" ]] && break
  sleep 0.05
done
[[ -S "$SOCKET" && -f "$READY" ]]
chmod 700 "$REPO"
chmod 600 "$LEDGER"

run_as() { local user=$1; shift; sudo -u "$user" "$@"; }

{
  echo "REQUESTER_UID=$REQUESTER_UID"
  echo "HOSTILE_UID=$HOSTILE_UID"
  echo "BROKER_PID=$BROKER_PID"
  echo "PRIVATE_ROOT=$PRIVATE_ROOT"
  echo "REPO=$REPO"
  echo "LEDGER=$LEDGER"
  echo "SOCKET=$SOCKET"
  echo "PROTECTED_REF=$REF"
  printf 'REQUESTER_ID='; id g4requester
  printf 'HOSTILE_ID='; id g4hostile
  printf 'GIT_VERSION='; git --version
  printf 'BROKER_BLOB='; git rev-parse HEAD:scripts/g4_broker.py
  printf 'G4_BLOB='; git rev-parse HEAD:agency_kernel/g4.py
  printf 'TEST_BLOB='; git rev-parse HEAD:tests/test_g4.py
  printf 'REPO_MODE='; stat -c '%a OWNER=%u GROUP=%g' "$REPO"
  printf 'LEDGER_MODE='; stat -c '%a OWNER=%u GROUP=%g' "$LEDGER"
  printf 'HOOKS_PATH='; git --git-dir "$REPO" config --get core.hooksPath
  printf 'FILE_PROTOCOL='; git --git-dir "$REPO" config --get protocol.file.allow
  printf 'ALTERNATES_PRESENT='; [[ -e "$REPO/objects/info/alternates" ]] && echo yes || echo no
  findmnt -T "$REPO" -o TARGET,SOURCE,FSTYPE,OPTIONS
  ss -ltnup || true
} > "$OUT/topology.txt" 2>&1

grep '^Cap' "/proc/$BROKER_PID/status" > "$OUT/broker_capabilities.txt"
run_as g4requester sh -c 'id; grep "^Cap" /proc/self/status' > "$OUT/requester_capabilities.txt" 2>&1
run_as g4hostile sh -c 'id; grep "^Cap" /proc/self/status' > "$OUT/hostile_capabilities.txt" 2>&1
run_as g4requester sh -c 'ip addr; ip route' > "$OUT/requester_network.txt" 2>&1
run_as g4hostile sh -c 'ip addr; ip route' > "$OUT/hostile_network.txt" 2>&1

INITIAL_OID=$(git --git-dir "$REPO" rev-parse "$REF")
printf '%s\n' "$INITIAL_OID" > "$OUT/initial_ref.txt"

# Positive legal Broker path.
run_as g4requester python "$CLIENT" --socket "$SOCKET" --request \
  "{\"action\":\"mutate\",\"expected_old_oid\":\"$INITIAL_OID\",\"files\":{\"A.txt\":\"positive\"},\"possible_effects\":[\"$REF_EFFECT\",\"$A_EFFECT\"]}" \
  > "$OUT/positive.json" 2> "$OUT/positive.stderr"
printf '0\n' > "$OUT/positive.exit"
grep -q '"allowed": true' "$OUT/positive.json"
POSITIVE_ADMISSION=$(python -c 'import json,sys; print(json.load(open(sys.argv[1]))["admission_id"])' "$OUT/positive.json")
POSITIVE_OID=$(git --git-dir "$REPO" rev-parse "$REF")
[[ "$POSITIVE_OID" != "$INITIAL_OID" ]]
[[ "$(git --git-dir "$REPO" show "$REF:A.txt")" = positive ]]

# Requester and secondary hostile identity cannot write protected storage directly.
set +e
run_as g4requester git --git-dir "$REPO" update-ref "$REF" "$INITIAL_OID" "$POSITIVE_OID" >"$OUT/requester_direct_ref.stdout" 2>"$OUT/requester_direct_ref.stderr"
REQ_REF_RC=$?
run_as g4hostile git --git-dir "$REPO" update-ref "$REF" "$INITIAL_OID" "$POSITIVE_OID" >"$OUT/hostile_direct_ref.stdout" 2>"$OUT/hostile_direct_ref.stderr"
HOST_REF_RC=$?
run_as g4requester sh -c "printf attack >> '$REPO/packed-refs'" >"$OUT/requester_storage.stdout" 2>"$OUT/requester_storage.stderr"
REQ_STORAGE_RC=$?
run_as g4hostile sh -c "mkdir -p '$REPO/hooks'; printf '#!/bin/sh\nexit 0\n' > '$REPO/hooks/update'" >"$OUT/hostile_hook.stdout" 2>"$OUT/hostile_hook.stderr"
HOOK_RC=$?
set -e
printf '%s\n' "$REQ_REF_RC" > "$OUT/requester_direct_ref.exit"
printf '%s\n' "$HOST_REF_RC" > "$OUT/hostile_direct_ref.exit"
printf '%s\n' "$REQ_STORAGE_RC" > "$OUT/requester_storage.exit"
printf '%s\n' "$HOOK_RC" > "$OUT/hostile_hook.exit"
[[ "$REQ_REF_RC" -ne 0 && "$HOST_REF_RC" -ne 0 && "$REQ_STORAGE_RC" -ne 0 && "$HOOK_RC" -ne 0 ]]
[[ "$(git --git-dir "$REPO" rev-parse "$REF")" = "$POSITIVE_OID" ]]

# Forged principal/credential-shaped input cannot authenticate a hostile peer.
run_as g4hostile python "$CLIENT" --socket "$SOCKET" --request \
  "{\"action\":\"mutate\",\"declared_principal\":\"alice\",\"broker_token\":\"forged\",\"files\":{\"A.txt\":\"forged\"},\"possible_effects\":[\"$REF_EFFECT\",\"$A_EFFECT\"]}" \
  > "$OUT/forged_identity.json" 2> "$OUT/forged_identity.stderr"
printf '0\n' > "$OUT/forged_identity.exit"
grep -q '"allowed": false' "$OUT/forged_identity.json"
grep -q 'missing_authentication_context' "$OUT/forged_identity.json"

# Admission bypass / forged admission ID.
run_as g4requester python "$CLIENT" --socket "$SOCKET" --request \
  '{"action":"execute_admission","admission_id":"forged-admission"}' \
  > "$OUT/bypass_admission.json" 2> "$OUT/bypass_admission.stderr"
printf '0\n' > "$OUT/bypass_admission.exit"
grep -q 'admission_absent' "$OUT/bypass_admission.json"

# Reuse consumed positive admission.
run_as g4requester python "$CLIENT" --socket "$SOCKET" --request \
  "{\"action\":\"execute_admission\",\"admission_id\":\"$POSITIVE_ADMISSION\"}" \
  > "$OUT/reuse_admission.json" 2> "$OUT/reuse_admission.stderr"
printf '0\n' > "$OUT/reuse_admission.exit"
grep -q 'admission_consumed' "$OUT/reuse_admission.json"

# O1 admitted, replacement/config/hooks/alternates-shaped fields are not execution input.
run_as g4requester python "$CLIENT" --socket "$SOCKET" --request \
  "{\"action\":\"mutate\",\"expected_old_oid\":\"$POSITIVE_OID\",\"files\":{\"A.txt\":\"O1\"},\"replacement_files\":{\"B.txt\":\"O2\"},\"git_config\":\"core.hooksPath=/tmp/evil\",\"alternates\":\"/tmp/evil\",\"possible_effects\":[\"$REF_EFFECT\",\"$A_EFFECT\"]}" \
  > "$OUT/o1_o2_config.json" 2> "$OUT/o1_o2_config.stderr"
printf '0\n' > "$OUT/o1_o2_config.exit"
grep -q '"allowed": true' "$OUT/o1_o2_config.json"
[[ "$(git --git-dir "$REPO" show "$REF:A.txt")" = O1 ]]
set +e
git --git-dir "$REPO" show "$REF:B.txt" >/dev/null 2>&1
B_PRESENT_RC=$?
set -e
[[ "$B_PRESENT_RC" -ne 0 ]]
[[ "$(git --git-dir "$REPO" config --get core.hooksPath)" != /tmp/evil ]]
[[ ! -e "$REPO/objects/info/alternates" ]]
O1_OID=$(git --git-dir "$REPO" rev-parse "$REF")

# UNKNOWN effects and over-broad envelope deny before protected-ref mutation.
run_as g4requester python "$CLIENT" --socket "$SOCKET" --request \
  "{\"action\":\"mutate\",\"expected_old_oid\":\"$O1_OID\",\"files\":{\"A.txt\":\"unknown\"}}" \
  > "$OUT/unknown_effects.json" 2> "$OUT/unknown_effects.stderr"
printf '0\n' > "$OUT/unknown_effects.exit"
grep -q 'unknown_possible_effects' "$OUT/unknown_effects.json"
run_as g4requester python "$CLIENT" --socket "$SOCKET" --request \
  "{\"action\":\"mutate\",\"expected_old_oid\":\"$O1_OID\",\"files\":{\"A.txt\":\"over\"},\"possible_effects\":[\"$REF_EFFECT\",\"$A_EFFECT\",\"PATH(secret.txt)\"]}" \
  > "$OUT/overbroad.json" 2> "$OUT/overbroad.stderr"
printf '0\n' > "$OUT/overbroad.exit"
grep -q 'effect_envelope_exceeded' "$OUT/overbroad.json"
[[ "$(git --git-dir "$REPO" rev-parse "$REF")" = "$O1_OID" ]]

# Stale CAS/admission state denies.
run_as g4requester python "$CLIENT" --socket "$SOCKET" --request \
  "{\"action\":\"mutate\",\"expected_old_oid\":\"$INITIAL_OID\",\"files\":{\"A.txt\":\"stale\"},\"possible_effects\":[\"$REF_EFFECT\",\"$A_EFFECT\"]}" \
  > "$OUT/stale_ref.json" 2> "$OUT/stale_ref.stderr"
printf '0\n' > "$OUT/stale_ref.exit"
grep -q 'stale_ref' "$OUT/stale_ref.json"

# Alternate environment/path attacks remain unable to reach the protected repo.
set +e
run_as g4hostile env GIT_CONFIG_GLOBAL=/tmp/evil.gitconfig GIT_ALTERNATE_OBJECT_DIRECTORIES=/tmp/objects git --git-dir "$REPO" rev-parse "$REF" >"$OUT/alternate_env.stdout" 2>"$OUT/alternate_env.stderr"
ALT_RC=$?
run_as g4hostile python -c 'import socket; s=socket.socket(); s.settimeout(1); s.connect(("127.0.0.1", 43178))' >"$OUT/network.stdout" 2>"$OUT/network.stderr"
NET_RC=$?
set -e
printf '%s\n' "$ALT_RC" > "$OUT/alternate_env.exit"
printf '%s\n' "$NET_RC" > "$OUT/network.exit"
[[ "$ALT_RC" -ne 0 && "$NET_RC" -ne 0 ]]

{
  printf 'FINAL_REF='; git --git-dir "$REPO" rev-parse "$REF"
  printf 'FINAL_TREE='; git --git-dir "$REPO" rev-parse "$REF^{tree}"
  printf 'FINAL_FILES='; git --git-dir "$REPO" ls-tree -r --name-only "$REF" | tr '\n' ','; echo
  printf 'A_CONTENT='; git --git-dir "$REPO" show "$REF:A.txt"
  printf 'LEDGER_SHA256='; sha256sum "$LEDGER" | awk '{print $1}'
} > "$OUT/final_state.txt"

set +x
find "$OUT" -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > "$OUT/SHA256SUMS"
