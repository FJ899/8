# Evidence-main accidental placeholder and exact restoration — 2026-09-06

During F040 local-failure evidence handling, an assistant-side GitHub write mistakenly created a placeholder file directly on `FJ899/8 main`, producing transient commit `d89dc46337d1d1417606dc1e54a9b635055cd62f` with parent `9b36a8d0f4a938442939320a46ad44ceaba39e3c`.

This was a process error. It was detected immediately before any dependent evidence was based on the transient main.

The `main` branch ref was then restored exactly to the prior frozen evidence-main commit:

`9b36a8d0f4a938442939320a46ad44ceaba39e3c`

Fresh read after restoration confirmed exact main HEAD `9b36a8d0f4a938442939320a46ad44ceaba39e3c` and tree `df807db7003dfd201e9be4d5927472e515a2e737`.

The transient placeholder commit is not current main authority and must not be used as an evidence base. Subsequent F040 failure/correction evidence branches are based on the restored exact frozen main.

Disposition: `ACCIDENTAL EVIDENCE-MAIN WRITE = DETECTED / EXACT REF RESTORED`.

No ScriptOps mutation, merge, deployment, release, tag, canonical effect, status promotion, X1B reopen, or V1 authority resulted from this incident.
