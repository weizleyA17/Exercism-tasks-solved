def is_triangle(sides):
    a, b, c = sides
    # 1. Garante que nenhum lado é zero ou negativo
    # 2. Garante a regra da desigualdade triangular
    return (a > 0 and b > 0 and c > 0) and (a + b >= c and b + c >= a and a + c >= b)


def equilateral(sides):
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not is_triangle(sides):
        return False
    return (sides[0] == sides[1] or
            sides[1] == sides[2] or
            sides[2] == sides[0])


def scalene(sides):
    if not is_triangle(sides):
        return False
    return (sides[0] != sides[1] and
            sides[1] != sides[2] and
            sides[0] != sides[2])