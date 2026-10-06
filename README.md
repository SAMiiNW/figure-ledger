# Figure Ledger

Figure Ledger turns context-bound public figures into a consumable policy decision on GenLayer. It is not a generic calculator. Every sheet freezes a metric, unit, reporting period, approved authority set, arithmetic operation, threshold policy, beneficiary and concrete consequence before evidence is reviewed.

## Trust boundary

1. The governor registers an authority name and exact HTTPS origin/path prefix.
2. An owner opens a sheet with two to five registered authorities and names an independent auditor and beneficiary.
3. The auditor submits one source per authority.
4. Validators independently fetch a frozen source snapshot, recompute SHA-256 receipts, and verify the proposed integer plus exact value, metric, unit and reporting-period quotes.
5. Deterministic contract code performs `SUM`, `DIFFERENCE`, or `RATIO_BPS`, then applies `AT_LEAST`, `AT_MOST`, or `EQUALS`.
6. Only the named beneficiary can consume an `AUTHORIZED` result, and only once.

The included North and South authorities, wallets and evidence files are operator-controlled demonstration fixtures. They prove enforcement and reproducibility; they are not represented as independent external institutions.

## Verified deployment

| Item | Value |
|---|---|
| Public app | https://figure-ledger.pages.dev/ |
| Network | GenLayer Studio Next, chain `61997` |
| Contract | `0x29235EFA4319eD831CFEF340d1Fab4d726bc3A17` |
| Deployment tx | `0x2c87fc7a1381a2e7350bc7763ce9dd405578ef7abbb674c7a5c3509fe24a9d6c` |
| Live verification tx | `0x9951c36c29b2d10cfdfee0ac8d031d4fd1e4d0db33257ae7a6b2c0ed6ad4bb85` |
| Live consumption tx | `0xcf489787f79db12daa323204d65e132a436493c201c82bd47c80270feb0c835e` |
| Stored outcome | `200 requests`, `AUTHORIZED`, `CONSUMED` |

The deployed contract source matches `contracts/contract.py` byte for byte. See `evidence/deployment-verification.json` and `evidence/live-run.json`.

## Tests

```text
python -m pytest -q
genvm-lint check contracts/contract.py
python scripts/verify_deployment.py
```

The test suite covers role authorization, authority URL binding, frozen receipt mismatches, prompt-injection rejection, contextual quote checks, denial, beneficiary authorization and replay protection.
