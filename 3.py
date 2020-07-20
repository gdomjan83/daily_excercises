def create_dict():
    num = int(input("Add argument: "))
    result = {}
    for item in range(1, num + 1):
        result.update({item: item ** 2})
    return result

print(create_dict())
