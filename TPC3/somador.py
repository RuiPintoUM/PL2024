import re
import fileinput

stdin = "\n".join(fileinput.input())

expressao = '(=|[O,o][F,f][F,f]|[O,o][N,n]|\d+)'
symbols = re.findall(expressao, stdin, flags=re.IGNORECASE)

Soma = 0
Estado = True

for symbol in symbols:
    if symbol.lower() == "on":
        Estado = True

    elif symbol.lower() == "off":
        Estado = False

    elif symbol == "=":
        print(Soma)  

    elif symbol.isdigit() and Estado:
        Soma += int(symbol)
    