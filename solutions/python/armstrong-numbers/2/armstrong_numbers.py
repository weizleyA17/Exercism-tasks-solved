def is_armstrong_number(number):
    num = str(number)
    digits = len(num)
    result = 0
    for digit in num:
        result+= int(digit) ** digits
    if result == number :
        return True
    else:
        return False
        