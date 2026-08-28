#!/usr/bin/env bash
set -u
set -o pipefail

OUT="${1:-g1-evidence}"
mkdir -p "$OUT/raw" "$OUT/state"
exec > >(tee "$OUT/raw/driver.stdout") 2> >(tee "$OUT/raw/driver.stderr" >&2)

run() {
  local name="$1"; shift
  printf '%q ' "$@" > "$OUT/raw/${name}.command"
  printf '\n' >> "$OUT/raw/${name}.command"
  set +e
  "$@" > >(tee "$OUT/raw/${name}.stdout") 2> >(tee "$OUT/raw/${name}.stderr" >&2)
  local rc=$?
  set -e
  printf '%s\n' "$rc" > "$OUT/raw/${name}.exit_code"
  return "$rc"
}
set -e

{
  echo "GITHUB_REPOSITORY=${GITHUB_REPOSITORY:-<unset>}"
  echo "GITHUB_SHA=${GITHUB_SHA:-<unset>}"
  echo "GITHUB_RUN_ID=${GITHUB_RUN_ID:-<unset>}"
  echo "GITHUB_RUN_ATTEMPT=${GITHUB_RUN_ATTEMPT:-<unset>}"
  echo "RUNNER_NAME=${RUNNER_NAME:-<unset>}"
  echo "RUNNER_OS=${RUNNER_OS:-<unset>}"
  echo "RUNNER_ARCH=${RUNNER_ARCH:-<unset>}"
  echo "RUNNER_ENVIRONMENT=${RUNNER_ENVIRONMENT:-<unset>}"
  echo "HEAD=$(git rev-parse HEAD)"
  echo "TREE=$(git rev-parse 'HEAD^{tree}')"
  echo "REMOTE=$(git remote get-url origin)"
  echo "UID=$(id -u)"
  echo "GID=$(id -g)"
  echo "GROUPS=$(id -G)"
  echo "UNAME=$(uname -a)"
  echo "PYTHON=$(python --version 2>&1)"
} | tee "$OUT/execution_instance.txt"

cat /proc/self/status > "$OUT/raw/proc-self-status.txt"
cat /proc/mounts > "$OUT/raw/mounts.txt"
if command -v capsh >/dev/null 2>&1; then capsh --print > "$OUT/raw/capabilities.txt"; else grep '^Cap' /proc/self/status > "$OUT/raw/capabilities.txt"; fi
if command -v ip >/dev/null 2>&1; then ip addr show > "$OUT/raw/ip-addr.txt"; ip route show > "$OUT/raw/ip-route.txt"; else cat /proc/net/route > "$OUT/raw/ip-route.txt"; fi
cat /etc/resolv.conf > "$OUT/raw/resolv.conf.txt"
cp .github/workflows/g1-evidence.yml "$OUT/workflow.yml"
git ls-tree HEAD .github/workflows/g1-evidence.yml scripts/run_g1_ci_evidence.sh scripts/g1_evidence_entry.py scripts/capture_g1_evidence.py tests/fixtures/g1_hostile_pythonpath/json.py agency_kernel/g1.py > "$OUT/candidate_blobs.txt"

HOSTILE_DIR="$PWD/tests/fixtures/g1_hostile_pythonpath"
MARKER="$PWD/$OUT/raw/HOSTILE_JSON_EXECUTED"
rm -f "$MARKER"
export AK_G1_HOSTILE_MARKER="$MARKER"
export PYTHONPATH="$HOSTILE_DIR${PYTHONPATH:+:$PYTHONPATH}"

run hostile_isolated python -I scripts/g1_evidence_entry.py --output-dir "$OUT/state"
if test -e "$MARKER"; then
  echo "HOSTILE_MODULE_EXECUTED=1" | tee "$OUT/hostile_pythonpath.txt"
  exit 91
else
  echo "HOSTILE_MODULE_EXECUTED=0" | tee "$OUT/hostile_pythonpath.txt"
fi
printf 'HOSTILE_PYTHONPATH=%s\n' "$PYTHONPATH" >> "$OUT/hostile_pythonpath.txt"

find "$OUT" -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > "$OUT/SHA256SUMS"
