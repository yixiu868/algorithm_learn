# encoding: utf-8


def fabonacci(i):
    if 1 == i or 2 == i:
        return 1
    else:
        return fabonacci(i - 1) + fabonacci(i - 2)


if '__main__' == __name__:
    print(fabonacci(1))
    print(fabonacci(2))
    print(fabonacci(3))
    print(fabonacci(4))
    print(fabonacci(5))
    print(fabonacci(8))

