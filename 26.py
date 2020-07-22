def add_numbers(*arg):
    total = 0
    args = [*arg]
    for number in args: 
        total += number
    return total
    

print(add_numbers(43, 32, 11, 100))