def dict_square():
    result = {}
    for i in range(1, 21):
        result.update({i: i ** 2})
    return result

print(dict_square())
