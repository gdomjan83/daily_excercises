def printy(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 == len2:
        print(f"{str1}\n{str2}")
    else:
        print(max(str1, str2, key = len))
    return True

printy("nort", "good")

    

