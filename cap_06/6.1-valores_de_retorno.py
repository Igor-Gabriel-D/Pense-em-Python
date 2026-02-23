import math

def area(radius):
    return radius * math.pi ** 2

print(area(1))


def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


print(absolute_value(-5))
