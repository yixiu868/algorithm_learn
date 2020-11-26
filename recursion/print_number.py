# encoding: utf-8


def countdown(i):
    """
    递归打印
    :param i:
    :return:
    """
    if i <= 0:
        return

    print(i)
    if i > 1:
        countdown(i-1)


if '__main__' == __name__:
    countdown(10)
    print('==================')
    countdown(5)
    print('===============---')
    countdown(-1)

