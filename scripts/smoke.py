import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.types import TransactionStatus
R=Path(__file__).parents[1];env=(R.parents[3]/'accounts.env').read_text();address=json.loads((R/'deployment.json').read_text())['contractAddress']
def acc(n):return create_account(account_private_key=re.search(rf'^ACCOUNT_{n}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',env,re.M).group(1).strip())
def client(n):return create_client(chain=studionet,account=acc(n))
def write(n,name,args):
 c=client(n);tx=c.write_contract(address=address,function_name=name,args=args);print(name+'_tx='+str(tx),flush=True);r=c.wait_for_transaction_receipt(transaction_hash=tx,status=TransactionStatus.FINALIZED,retries=180,interval=5000,full_transaction=True);leader=(r.get('consensus_data',{}).get('leader_receipt')or[{}])[0];assert r.get('result_name')=='MAJORITY_AGREE' and leader.get('execution_result')=='SUCCESS';return str(tx)
sid='TOTAL-'+str(int(time.time()));sources=['https://raw.githubusercontent.com/SAMiiNW/figure-ledger/main/docs/evidence/north-count.md','https://cdn.jsdelivr.net/gh/SAMiiNW/figure-ledger@main/docs/evidence/south-count.md'];tx={'open':write(1,'open_sheet',[sid,acc(2).address,'September service total',['North completed requests','South completed requests'],'SUM',200]),'verify':write(2,'verify_sheet',[sid,sources])};state=client(1).read_contract(address=address,function_name='get_sheet',args=[sid]);assert state['state']=='MATCH' and state['computed_result']==200 and state['values']==[120,80];proof={'sheetId':sid,'transactions':tx,'state':state,'walletDisclosure':'Both wallets and evidence files are operator-controlled fixtures.'};(R/'evidence'/'live-run.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof,indent=2),flush=True)
