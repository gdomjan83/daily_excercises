bin = input("Enter binary numbers: ").split(",")
result = []
for x in bin:
    if int(x, base = 2) % 5 == 0:
        result.append(x)
print(",".join(result))