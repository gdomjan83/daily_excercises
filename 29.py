def concatenate(*args):
    result = ""
    args = [*args]
    for i in args:
        result += i
    return result

print(concatenate("This", "Is", "Good!"))

