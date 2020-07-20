a = input("Enter words: ").split(" ")
b = list(set(a))
b.sort()
print(" ".join(b))