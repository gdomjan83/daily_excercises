balance = 0
while True:
    inp = input("Enter transaction: ").split(" ")
    if inp[0] == "":
        break
    if inp[0] == "D":
        balance += int(inp[1])
    elif inp[0] == "W":
        balance -= int(inp[1])
print(balance)
