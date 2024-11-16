from pyfuck import compile_bce0, compile_b_comma, compile_final
import sys

with open(sys.argv[1], "rb") as f:
	code_bytes = f.read()

code_bits = bin(int.from_bytes(code_bytes))[2:].replace("0", "(").replace("1", ")")
nice_code = f'exec(int("{code_bits}".replace("(","0").replace(")","1"),2).to_bytes({len(code_bytes)}))'

encoded, args = compile_bce0(nice_code, "exc(%0)b,")
encoded = f"""exec("{encoded}"%{args})"""
encoded, args = compile_b_comma(encoded)
encoded = f"""exec('{encoded}'%{args})"""
encoded, args = compile_bce0(encoded)
encoded = f"""exec("{encoded}"%{args})"""
encoded, args = compile_final(encoded)
encoded = f"""exec('''{encoded}'''{args})"""

encoded = 'exec("' + encoded.translate({
	ord("e"): 9,
	ord("x"): 11,
	ord("c"): 12,
	ord("("): 28,
	ord("'"): 29,
	ord("%"): 30,
	ord("0"): 31,
	ord(")"): 32
}) + '".translate("         e xc               (\'%0)"))'

assert sum(not c.isspace() for c in encoded) == 30

print(encoded)
