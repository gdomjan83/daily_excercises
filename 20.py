class DivideSeven():
    def generator(self, n):
        for i in range(n + 1):
            if i % 7 == 0:
                yield i

obj = DivideSeven()
rng = int(input("Please enter the number: "))
for j in obj.generator(rng):
    print(j)

