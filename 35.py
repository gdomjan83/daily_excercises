def sq_list():
    result = [i ** 2 for i in range (1, 21)]
    return result[-5:]

print(sq_list())