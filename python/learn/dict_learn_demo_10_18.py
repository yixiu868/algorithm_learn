# 字典练习


def test001():
    """
    添加键值对
    :return:
    """
    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0)

    # 指定key添加元素
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)

    # 删除键值对
    del alien_0['points']
    print(alien_0)


def test002():
    """
    遍历所有键值对
    :return:
    """
    user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi'
    }

    # 遍历
    for key, value in user_0.items():
        print('Key: ' + key)
        print('Value: ' + value)
        print('-----------')

    # 遍历所有键
    for name in user_0.keys():
        print(name.title())


if '__main__' == __name__:
    # test001()
    test002()
