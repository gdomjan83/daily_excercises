from math import sqrt

def robot_move():
    x = 0
    y = 0
    while True:
        inp = input("Enter command: ").split(" ")
        if inp[0] == "":
            break
        inp[0] = str(inp[0])
        inp[1] = int(inp[1])
        if inp[0] == "UP":
            y += inp[1]
        if inp[0] == "DOWN":
            y -= inp[1]
        if inp[0] == "RIGHT":
            x += inp[1]
        if inp[0] == "LEFT":
            x -= inp[1]
    return round(sqrt(x ** 2 + y ** 2))

print(robot_move())
