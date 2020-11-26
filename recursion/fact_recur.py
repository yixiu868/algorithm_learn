# encoding: utf-8

"""
递归实现阶乘
"""


def fact(i):
    if 1 == i:
        return 1
    else:
        return i * fact(i - 1)


if '__main__' == __name__:
    print(fact(5))
    print(fact(10))

