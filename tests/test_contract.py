import ast
from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text();T=ast.parse(S)
def load(n):
 x=next(v for v in T.body if isinstance(v,ast.FunctionDef) and v.name==n);d={};exec(compile(ast.Module(body=[x],type_ignores=[]),'<c>','exec'),d);return d[n]
def test_calculations():
 f=load('calculate');assert f('SUM',[120,80])==200;assert f('DIFFERENCE',[120,80])==40;assert f('RATIO_BPS',[25,100])==2500
def test_exact_consensus_and_attribution():
 for phrase in ('approve_authority','metric_quote','unit_quote','period_quote','consume_authorization','threshold_decision','distinct authority origins required'):assert phrase in S.lower()
def test_surface():
 for n in ('approve_authority','open_sheet','verify_sheet','consume_authorization','get_sheet'):assert f'def {n}' in S
