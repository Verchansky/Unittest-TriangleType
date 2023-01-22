from math import sqrt


def triangleType(a, b, c):
    if a == b == c:
        return "Треугольник равносторонний"
    elif a == b and b != c or a == c and a != b or b == c and b != a:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник разносторонний"

#Равносторонний
def equilateralTriange(a, b, c):
    if a == b == c:
        return True
    else:
        return False


# Равнобедренный
def isoscelesTriangle(a, b, c):
    if a == b and b != c or a == c and a != b or b == c and b != a:
        return True
    else:
        return False


# Разносторонний
def versatileTriangle(a, b, c):
    if (a != b) and (b != c):
        return True
    else:
        return False


# Проверка условия
def checkNumber(a, b, c):
    status = bool(False)
    if (a + b >= c and a + c >= b and b + c >= a) and (a > 0 and b > 0 and c > 0):
        status = True
        return status
    else:
        return status


# Функция вычисления площади треугольника по формуле Герона
def getSquare(a, b, c):
    p = (a + b + c) / 2
    square = sqrt(p * (p - a) * (p - b) * (p - c))
    return square


def main():
    print('Введите стороны треугольника: ')
    a, b, c = map(int, input().split())


if __name__ == "__main__":
    main()
