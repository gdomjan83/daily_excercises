data = []
while True:
    inp = input("Enter name,age,score: ").split(",")
    if inp[0] == "":
        break
    inp[1] = int(inp[1])
    inp[2] = int(inp[2])
    data.append(tuple(inp))
data = sorted(data)
print(data)
