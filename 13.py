result = [0, 0]
inp = input("Enter sentence: ")
for i in inp:
    if i.isalpha():
        result[0] += 1
    elif i.isdigit():
        result[1] += 1
print(f"LETTERS {result[0]}\nDIGITS {result[1]}")

