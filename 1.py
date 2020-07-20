def find_number():
    for item in range(2000, 3201):
        if (item % 7 == 0) and (item % 5 != 0): #szám megtalálása ami osztható 7-tel, de nem osztható 5-tel, és egy sorba nyomtatni őket
            print(item, end=",")


find_number()




