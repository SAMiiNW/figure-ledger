import json, re, time
from dataclasses import replace
from pathlib import Path
from genlayer_py import create_account, create_client
from genlayer_py.chains import studio_devnet

ROOT = Path(__file__).parents[1]
env = (ROOT.parents[3] / "accounts.env").read_text()
deployment = json.loads((ROOT / "deployment.json").read_text())
contract = deployment["contractAddress"]
commit = deployment["sourceCommit"]
chain = replace(studio_devnet, name="GenLayer Studio Next", rpc_urls={"default": {"http": ["https://studio-next.genlayer.com/api"]}})

def account(number):
    key = re.search(rf'^ACCOUNT_{number}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)', env, re.M).group(1).strip()
    return create_account(account_private_key=key)

def client(number): return create_client(chain=chain, account=account(number))

def write(number, label, function, args, intelligent=False):
    c = client(number)
    fees = c.estimate_transaction_fees({"leader_timeunits_allocation": 500 if intelligent else 180, "validator_timeunits_allocation": 650 if intelligent else 360})
    tx = c.write_contract(address=contract, function_name=function, args=args, fees=fees)
    print(label + "_tx=" + str(tx), flush=True)
    c.wait_for_transaction_receipt(transaction_hash=tx, wait_until="finalized", retries=300, interval=3000, full_transaction=True)
    return str(tx)

raw_prefix = f"https://raw.githubusercontent.com/SAMiiNW/figure-ledger/{commit}/docs/evidence/"
cdn_prefix = f"https://cdn.jsdelivr.net/gh/SAMiiNW/figure-ledger@{commit}/docs/evidence/"
sources = [raw_prefix + "north-count.md", cdn_prefix + "south-count.md"]
sheet_id = "SEPT-AUTH-" + str(int(time.time()))
transactions = {}
transactions["approveNorth"] = write(1, "APPROVE_NORTH", "approve_authority", ["NORTH_OPS", "North Service Operations demo authority", raw_prefix])
transactions["approveSouth"] = write(1, "APPROVE_SOUTH", "approve_authority", ["SOUTH_AUDIT", "South Service Audit demo authority", cdn_prefix])
transactions["open"] = write(1, "OPEN", "open_sheet", [sheet_id, account(2).address, account(3).address, "September service authorization", "completed service requests", "requests", "2026-09-01", "2026-09-30", ["NORTH_OPS", "SOUTH_AUDIT"], "SUM", "AT_LEAST", 200, "Authorize the October maintenance tranche for the named beneficiary"])
transactions["verify"] = write(2, "VERIFY", "verify_sheet", [sheet_id, sources], intelligent=True)
transactions["consume"] = write(3, "CONSUME", "consume_authorization", [sheet_id])
state = client(1).read_contract(address=contract, function_name="get_sheet", args=[sheet_id])
if state["state"] != "CONSUMED" or state["decision"] != "AUTHORIZED" or state["computed_result"] != 200: raise RuntimeError("unexpected stored state: " + json.dumps(state))
proof = {"sheetId": sheet_id, "transactions": transactions, "sources": sources, "state": state, "walletDisclosure": "All demo wallets and authority files are operator-controlled fixtures; the contract nevertheless enforces registered origins, exact context, source receipts, independent auditor and beneficiary roles."}
(ROOT / "evidence" / "live-run.json").write_text(json.dumps(proof, indent=2) + "\n")
print(json.dumps(proof, indent=2), flush=True)
