from pathlib import Path
HTML=(Path(__file__).parents[1]/'docs'/'index.html').read_text()
def test_complete_browser_workflow():
 for item in ('id="connect"','id="open"','id="verify"','id="load"','id="demo"','FINALIZED','get_sheet'):assert item in HTML
def test_machine_ledger_identity():
 assert 'class="machine"' in HTML and 'SOURCE DRAWER' in HTML
 assert 'class="readout"' in HTML and 'class="bay operator"' in HTML
