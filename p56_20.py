import math
from sympy import *

x = Symbol('x')


def newton(fx, x0, error_margin):
    # 将f'(x)函数lambda化
    f_derivative = lambdify(x, diff(fx, x))
    error = error_margin + 1
    while error > error_margin:
        # 牛顿迭代格式公式
        x1 = x0 - fx.subs(x, x0) / f_derivative(x0)
        error = abs(x0 - x1)
        x0 = x1
    return x0


def is_converge_to_0(value, error_margin=0.0001):
    return abs(value) <= error_margin


def find_max_delta(start, step, fx, error_margin=0.0001):
    current = start
    for i in range(10):
        if is_converge_to_0(newton(fx, current + step, error_margin)):
            current += step
            continue
        else:
            print(f'当x0取{current}时f(x)收敛到0，当x0取{current + step}时f(x)收敛到根号3')
            break

    if step <= error_margin:
        return current, step
    else:
        find_max_delta(current, step / 10, fx, error_margin)


if __name__ == '__main__':
    fx = x ** 3 / 3 - x
    print(f'''当x0=1.2时f(x)收敛到{newton(fx, 1.2, 0.0001)}
当x0=0.2时f(x)收敛到{newton(fx, 0.2, 0.0001)}
当x0=-1.2时f(x)收敛到{newton(fx, -1.2, 0.0001)}
''')

    find_max_delta(0.1, 0.1, fx)
