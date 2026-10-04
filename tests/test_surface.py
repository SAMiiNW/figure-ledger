from pathlib import Path
HTML=(Path(__file__).parents[1]/'docs'/'index.html').read_text()
def test_complete_browser_workflow():
 for item in ('CONNECT WALLET','OPEN SHEET','VERIFY FIGURES','LOAD RECEIPT','RUN 120 + 80 DEMO','FINALIZED','get_sheet'):assert item in HTML
def test_calculator_identity():
 assert 'class="formula"' in HTML and 'Show your working.' in HTML
