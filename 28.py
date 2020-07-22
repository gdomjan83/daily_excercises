def convert(*args):
    total = 0
    args = [*args]
    for number in args:
        total += int(number)
    return total

print(convert("4", "10", "41"))