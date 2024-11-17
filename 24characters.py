import sys

with open(sys.argv[1], "r") as f:
	code = f.read()

# Downgrade to ASCII
code = f"exec({code.encode()})"

# Generate a payload using mostly \, x, and the hexadecimal alphabet. We pay 4 characters for ('').
code = "exec('" + "".join(f"\\x{c:02x}" for c in code.encode()) + "')"

# Generate \, x, and the hexadecimal alphabet from repr of a string. This takes 20 more characters.
class mktable:
    def __getitem__(self, c):
    	return {
            "\\": "     \t ",
            "x" : "    \x0b",
            "0" : "\u2000  ",
            "1" : "\u2001  ",
            "2" : "\u2002  ",
            "3" : "\u2003  ",
            "4" : "\u2004  ",
            "5" : "\u2005  ",
            "6" : "\u2006  ",
            "7" : "\u2007  ",
            "8" : "\u2008  ",
            "9" : "\u2009  ",
            "a" : "\u200a  ",
            "b" : "  \x0b  ",
            "c" : "  \x0c  ",
            "d" : "  \x1d  ",
            "e" : "  \x1e  ",
            "f" : "  \x1f  ",
        }.get(chr(c), f"     {chr(c)}  ")
code = code.translate(mktable())
code = f"exec(repr(\"{code}\")[6::8])"

assert sum(not c.isspace() for c in code) == 24
print(code)
