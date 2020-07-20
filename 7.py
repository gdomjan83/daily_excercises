x, y = map(int, input("Add 2 numbers: ").split(","))
result = []

for i in range(x):
    result.append([])
    for j in range(y):
        result[i].append(i * j)

print(result)
