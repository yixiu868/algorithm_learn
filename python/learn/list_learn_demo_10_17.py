# list常用方法练习


def test001():
    """
    pop()删除元素，从list末尾删除元素，并返回
    :return:
    """
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)

    # 删除末尾元素
    popped_motorcycle = motorcycles.pop()
    print(popped_motorcycle)
    print(motorcycles)

    print('-----------------------')
    # 删除指定位置元素
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print('删除前列表:', motorcycles)
    element2 = motorcycles.pop(1)
    print('删除第二个元素:', element2)
    print('删除后列表:', motorcycles)


def test002():
    """
    # 指定值删除元素
    :return:
    """
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print('列表删除前:', motorcycles)
    motorcycles.remove('suzuki')
    print('列表元素删除后:', motorcycles)


def test003():
    """
    对列表进行排序
    :return:
    """
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print('排序前:', cars)
    cars.sort()
    print('sort()排序后:', cars)
    cars.sort(reverse=True)
    print('sort(reverse=True)再次倒排:', cars)

    print("------------------")
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print('重新赋值cars:', cars)
    print('使用sorted排序:', sorted(cars))
    print('再次打印cars:', cars)


def test004():
    """
    foreach遍历
    :return:
    """

    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(magician.title() + ", that was a greate trick")

    # range()创建数字序列
    for value in range(1, 5):
        print(value)

    # 列表解析
    squares = [value ** 2 for value in range(1, 11)]
    print(squares)

    # 切片
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[0:3])


def test005():
    """
    复制列表
    :return:
    """
    my_foods = ['pizza', 'falafel', 'carrot cake']
    # 复制，开辟新的地址空间
    friend_foods = my_foods[:]

    print('My favorite foods are:')
    print("my_foods排序前:", my_foods)
    my_foods.sort()
    print("my_foods排序后:", my_foods)
    print("friend_foods:", friend_foods)

    # 引用，指向同一地址空间
    print('-------------------')
    friend_ref = my_foods
    my_foods.append('cannoli')
    friend_ref.append('ice cream')

    print('My favorite foods are:')
    print(my_foods)
    print('\nMy friend\'s favorite foods are:')
    print(friend_ref)


if '__main__' == __name__:
    # test001()
    # test002()
    # test003()
    # test004()
    test005()
