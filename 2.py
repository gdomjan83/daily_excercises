def fact():
    num = int(input("Factorial of: "))
    result = num
    while num > 1:
        result *= num - 1
        num -= 1
    return result

print(fact())