upper, lower = 0, 0
inp = input("Enter sentence: ")
for i in inp:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print(f"UPPER CASE {upper}\nLOWER CASE {lower}")

