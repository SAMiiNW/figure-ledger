# FIGURE LEDGER // OPERATOR MANUAL

## PURPOSE

Rebuild a numeric claim from public evidence. Do not ask validators whether a total *sounds right*. Ask them for exact source-bound integers, then let deterministic contract code perform the arithmetic.

```text
SOURCE DRAWER  ->  VALIDATOR EXTRACTION  ->  CONTRACT OPERATOR  ->  RECEIPT
 URLs              values + citations       SUM / Δ / ratio        MATCH
```

## CONTROL SURFACE

`OPEN LEDGER` fixes the labels, auditor, operation, and claimed result. `VERIFY SOURCES` retrieves distinct evidence URLs and stores one digest and citation set per extracted value. `LOAD BY SHEET ID` reproduces the completed calculation.

Supported operators:

- `SUM`: `A + B`
- `DIFFERENCE`: `A - B`
- `RATIO_BPS`: `(A × 10,000) / B`

Malformed figures, repeated sources, unsupported operations, unauthorized auditors, and replayed sheets are rejected.

## VERIFIED MACHINE

```text
PUBLIC      https://figure-ledger.pages.dev/
SOURCE      https://github.com/SAMiiNW/figure-ledger
CONTRACT    0x2c5Aaa83f41d008b6370B4DE7f4b4F30fb6Ea5d4
DEPLOYMENT  FINALIZED / MAJORITY_AGREE / SUCCESS
BROWSER     120 + 80 = 200 / MATCH
```

Receipts: `evidence/live-run.json` and `evidence/browser-run.json`

Source comparison: `evidence/deployment-verification.json`

## BENCH TEST

```text
python -m pytest -q
genvm-lint check contracts/contract.py
python scripts/verify_deployment.py
```

## FIXTURE LABEL

The sample counts, evidence pages, and demo wallets are operator-controlled. They demonstrate reproducibility; they are not independent data authorities.
