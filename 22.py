inp = input("Write a sentence:").split(" ")
inp2 = list(set(inp))
inp2.sort()
for word in inp2:
    print(f"{word}: {inp.count(word)}")
