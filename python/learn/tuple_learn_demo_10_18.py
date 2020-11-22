"""
元素基础练习
"""


def test001():
    """
    修改元组变量
    :return:
    """
    dimensions = (200, 5)
    print('Original dimensions:')
    for dimension in dimensions:
        print(dimension)

    dimensions = (400, 100)
    print('\nModified dimensions:')
    for dimension in dimensions:
        print(dimension)


if '__main__' == __name__:
    test001()

