def sq_tuple():
    result = [i ** 2 for i in range (1, 21)]
    return tuple(result)

print(sq_tuple())