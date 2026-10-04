# Figure Ledger

Figure Ledger is a source-bound calculator for claims that should be reproducible, not merely persuasive. A sheet names its inputs, fixes one deterministic operation, and records the claimed result. Validators retrieve distinct evidence sources and agree on every exact integer, citation index, and digest. Contract code recomputes the result and returns `MATCH` or `MISMATCH`.

The public application looks and behaves like an audit calculator. Users compose a sheet, paste evidence into a source drawer, verify it, and receive a numeric receipt. SUM, DIFFERENCE, and RATIO_BPS are intentionally bounded so reviewers can reproduce the arithmetic without trusting prose.

## Verified release

- Application: https://figure-ledger.pages.dev/
- Repository: https://github.com/SAMiiNW/figure-ledger
- StudioNet contract: `0x2c5Aaa83f41d008b6370B4DE7f4b4F30fb6Ea5d4`
- Deployment: `FINALIZED / MAJORITY_AGREE / SUCCESS`
- Public browser run: extracted `120` and `80`, recomputed `200`, and finalized `MATCH`

The public run used the exact canonical URL and recorded both finalized transaction hashes in `evidence/browser-run.json`.

## Checks

```text
python -m pytest -q
genvm-lint check contracts/contract.py
```

The sample counts and wallets are operator-controlled fixtures and are labelled accordingly.
