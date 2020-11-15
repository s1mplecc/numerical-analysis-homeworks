import math
from sympy import *

x = Symbol('x')


def newton(fx, x0, error_margin):
    f_derivative = lambdify(x, diff(fx, x))
    error = error_margin + 1
    while error > error_margin:
        x1 = x0 - fx.subs(x, x0) / f_derivative(x0)
        print(x1)
        error = abs(x0 - x1)
        x0 = x1


if __name__ == '__main__':
    newton(x ** 3 / 3 - x, 1.2, 0.0001)
    newton(x ** 3 / 3 - x, 0.2, 0.0001)
    newton(x ** 3 / 3 - x, -1.2, 0.0001)
