import hashlib, json, re
from dataclasses import replace
from pathlib import Path
from genlayer_py import create_account, create_client
from genlayer_py.chains import studio_devnet

ROOT = Path(__file__).parents[1]
env = (ROOT.parents[3] / "accounts.env").read_text()
key = re.search(r'^ACCOUNT_1_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)', env, re.M).group(1).strip()
chain = replace(studio_devnet, name="GenLayer Studio Next", rpc_urls={"default": {"http": ["https://studio-next.genlayer.com/api"]}})
client = create_client(chain=chain, account=create_account(account_private_key=key))
code = (ROOT / "contracts" / "contract.py").read_text()
fees = client.estimate_transaction_fees({"leader_timeunits_allocation": 250, "validator_timeunits_allocation": 500})
tx = client.deploy_contract(code=code, args=[], fees=fees)
print("deploy_tx=" + str(tx), flush=True)
receipt = client.wait_for_transaction_receipt(transaction_hash=tx, wait_until="finalized", retries=240, interval=3000, full_transaction=True)
address = receipt.get("data", {}).get("contract_address") or receipt.get("tx_data_decoded", {}).get("contractAddress") or receipt.get("to_address")
if not address: raise RuntimeError("finalized deployment returned no contract address: " + json.dumps(receipt, default=str)[:1200])
out = {"project": "Figure Ledger", "network": "GenLayer Studio Next", "chainId": 61997, "rpcUrl": "https://studio-next.genlayer.com/api", "explorerUrl": "https://explorer-studio-dev.genlayer.com", "contractAddress": address, "deploymentTransaction": str(tx), "sourceSha256": hashlib.sha256(code.encode()).hexdigest(), "sourceCommit": "e79eeda07456e17bba30a96e3570e9274c3bd84c", "repository": "https://github.com/SAMiiNW/figure-ledger"}
(ROOT / "deployment.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2), flush=True)
