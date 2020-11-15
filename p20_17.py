# 舍入误差与有效数
import math


# 从大到小（降序）顺序Sn
def descend_s_n(N):
    l = list(range(2, N))
    l.reverse()
    sn = 0
    for i in l:
        sn += 1 / (i * i - 1)
    return sn


# 从小到大（升序）顺序Sn
def ascend_s_n(N):
    sn = 0
    for i in range(2, N):
        sn += 1 / (i * i - 1)
    return sn


# 精确值
def accurate_s_n(N):
    return 0.5 * (1.5 - 1 / N - 1 / (N + 1))


# 有效位数
def effective_digits(accurate, approximate):
    e = abs(accurate - approximate)
    i = 0
    while e <= 0.5 * math.pow(0.1, i):
        i = i + 1
    return i


def s_n_by_10_pow_(power):
    N = int(math.pow(10, power))
    accurate_result = accurate_s_n(N)
    ascend_result = ascend_s_n(N)
    descend_result = descend_s_n(N)
    print(f'''
当N=10^{power}时，精确值为：{accurate_result}；
升序结果为：{ascend_result}，有效位数{effective_digits(accurate_result, ascend_result)}位；
降序结果为：{descend_result}，有效位数{effective_digits(accurate_result, descend_result)}位''')


if __name__ == '__main__':
    s_n_by_10_pow_(2)
    s_n_by_10_pow_(4)
    s_n_by_10_pow_(6)
