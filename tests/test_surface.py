from pathlib import Path
HTML=(Path(__file__).parents[1]/'docs'/'index.html').read_text()
def test_complete_browser_workflow():
 for item in ('id="connect"','id="open"','id="verify"','id="consume"','id="load"','until:\'finalized\'','get_sheet'):assert item in HTML
def test_context_bound_ledger_identity():
 for item in ('FREEZE THE CONTEXT','VERIFY AUTHORITY EVIDENCE','FINALIZED RECEIPT','NORTH_OPS','SOUTH_AUDIT','CONCRETE CONSEQUENCE'):assert item in HTML
