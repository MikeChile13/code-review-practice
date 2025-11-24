def addDigits(num):
    split = str(num)
    sumv = 0
    for char in split:
        sumv += int(char)
    return sumv
