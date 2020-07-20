inp = input("Enter numbers :").split(",")
result = [str(int(item) ** 2) for item in inp if int(item) % 2 != 0]
print(",".join(result))