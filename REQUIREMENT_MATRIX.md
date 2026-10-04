# Requirement matrix

| Requirement | Implementation | Proof |
|---|---|---|
| Extract exact figures from public evidence | `verify_sheet` retrieves every source and returns one integer per source | Contract tests and `evidence/live-run.json` |
| Preserve numeric provenance | URLs, labels, SHA-256 digests, citations, owner, and auditor are stored | `contracts/contract.py` and finalized receipt |
| Keep arithmetic deterministic | Contract code computes SUM, DIFFERENCE, or RATIO_BPS | Unit tests cover all operations and bounds |
| Provide a complete public workflow | Open, verify, lookup, wallet connection, and full demo are available | `https://figure-ledger.pages.dev/` |
| Prove the deployed artifact | Source hash matches the finalized StudioNet deployment | `evidence/deployment-verification.json` |
| Prove browser execution | Canonical public site reached `DEMO FINALIZED` with `MATCH` | `evidence/browser-run.json` |
