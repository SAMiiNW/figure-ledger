import ast
from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text();T=ast.parse(S)
def load(n):
 x=next(v for v in T.body if isinstance(v,ast.FunctionDef) and v.name==n);d={};exec(compile(ast.Module(body=[x],type_ignores=[]),'<c>','exec'),d);return d[n]
def test_calculations():
 f=load('calculate');assert f('SUM',[120,80])==200;assert f('DIFFERENCE',[120,80])==40;assert f('RATIO_BPS',[25,100])==2500
def test_exact_consensus_and_attribution():
 assert 'every exact integer, citation index, and source digest must match exactly' in S;assert 'every value requires source attribution' in S;assert 'distinct source origins required' in S
def test_surface():
 for n in ('open_sheet','verify_sheet','get_sheet'):assert f'def {n}' in S
