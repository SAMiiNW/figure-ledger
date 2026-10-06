import base64, hashlib, json
from dataclasses import replace
from pathlib import Path
from genlayer_py import create_client
from genlayer_py.chains import studio_devnet

ROOT = Path(__file__).parents[1]
deployment = json.loads((ROOT / "deployment.json").read_text())
chain = replace(studio_devnet, name="GenLayer Studio Next", rpc_urls={"default": {"http": ["https://studio-next.genlayer.com/api"]}})
client = create_client(chain=chain)
transaction = client.get_transaction(transaction_hash=deployment["deploymentTransaction"])
deployed = base64.b64decode(transaction["data"]["contract_code"], validate=True)
local = (ROOT / "contracts" / "contract.py").read_bytes()
result = {"contract": deployment["contractAddress"], "deploymentTransaction": deployment["deploymentTransaction"], "network": deployment["network"], "sourceSha256": hashlib.sha256(deployed).hexdigest(), "sourceMatches": deployed == local}
print(json.dumps(result, indent=2))
if not result["sourceMatches"]: raise RuntimeError("deployed contract source does not match repository source")
(ROOT / "evidence" / "deployment-verification.json").write_text(json.dumps(result, indent=2) + "\n")
