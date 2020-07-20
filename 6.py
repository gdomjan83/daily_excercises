import math

num = input("Add numbers: ")
lst = num.split(",")
c = 50
h = 30
result = []
for x in lst:
    y = str(math.floor(math.sqrt((2 * c * int(x)) / h)))
    result.append(y)

print(",".join(result))

