lst = []

while True:
    x = input("Enter line: ").upper()
    if (len(x) == 0):
        break
    lst.append(x)

for x in lst:
    print(x)
