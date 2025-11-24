def addDigits(num):
    if num < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    split = str(num)
    sumv = 0
    for char in split:
        sumv += int(char)
    return sumv
