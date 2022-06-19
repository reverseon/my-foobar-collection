import base64
from itertools import cycle
MSG = "D0kSHxQCC0FFU05bSlAGHFdXAElNSlACAV5aEQ8GHxJGTggWUwsSHhIEA1dSU0JBTRIHCF1EAB1G Sk1BSVtYFxwEDh4DAlcRWE5GCxQJB1dAEQMEBANGTggWUxsPBhgCBVdSU0JBTQUADFBfAB1GSk1B SUFXEgtGRldGCF1ZU05bSlAWB1wXUxM="
KEY = bytes("tnajwan26", "utf-8")

print(bytes(a ^ b for a, b in zip(base64.b64decode(MSG), cycle(KEY))))