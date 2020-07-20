result = []
for item in range(1000, 3001):
    even = 1
    for dig in str(item):
        if int(dig) % 2 != 0:
            even = 0
            break
    if even == 1:
        result.append(str(item))
print(",".join(result))
