import base64
import hashlib
import json
from pathlib import Path

from genlayer_py import create_client
from genlayer_py.chains import studionet

root = Path(__file__).parents[1]
deployment = json.loads((root / "deployment.json").read_text())
transaction = create_client(chain=studionet).get_transaction(
    transaction_hash=deployment["deploymentTransaction"]
)
deployed_source = base64.b64decode(transaction["data"]["contract_code"], validate=True)
local_source = (root / "contracts" / "contract.py").read_bytes()
leader_receipts = transaction.get("consensus_data", {}).get("leader_receipt") or [{}]
leader_receipt = leader_receipts[0] if isinstance(leader_receipts, list) else leader_receipts
status_changes = transaction.get("consensus_history", {}).get("current_status_changes") or []
status = transaction.get("status_name") or transaction.get("status")
if status is None and status_changes:
    status = status_changes[-1]
result = {
    "contract": deployment["contractAddress"],
    "deploymentTransaction": deployment["deploymentTransaction"],
    "status": status,
    "consensus": transaction.get("result_name"),
    "execution": leader_receipt.get("execution_result"),
    "sourceSha256": hashlib.sha256(deployed_source).hexdigest(),
    "sourceMatches": deployed_source == local_source,
}
print(json.dumps(result, indent=2))
assert result["status"] == "FINALIZED"
assert result["consensus"] == "MAJORITY_AGREE"
assert result["execution"] == "SUCCESS"
assert result["sourceMatches"]
(root / "evidence" / "deployment-verification.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
