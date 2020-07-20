import re
#pattern: legalább egy kisbetű, legalább egy nagybetű, legalább egy spec. karakter, legalább 1 szám, összesen 6-12 karakter
pattern = r"""^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[a-zA-z0-9$#@]{6,12}$"""
inp = input("Enter passwords: ").split(",")
result = []
match = None
for i in inp:
    match = re.fullmatch(pattern, i)
    if match != None:
        result.append(i)
        match = None
print(",".join(result))
