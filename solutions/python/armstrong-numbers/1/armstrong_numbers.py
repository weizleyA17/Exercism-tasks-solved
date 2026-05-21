def is_armstrong_number(number):
    num = str(number)
    digits = len(num)
    sum = 0
    for digit in num:
        sum+= int(digit) ** digits
    if sum == number :
        return True
    else:
        return False
        