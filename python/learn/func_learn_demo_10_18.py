# 函数基本使用


def test001(animal_type, pet_name):
    """
    位置参数
    :param animal_type:
    :param pet_name:
    :return:
    """
    print('I have a ' + animal_type + ".")
    print('My ' + animal_type + '\'s name is ' + pet_name.title() + ".")


def test002(*toppings):
    """
    传递任意数量的实参
    :param toppings:
    :return:
    """
    print(toppings)


def test003(first, last, **user_info):
    """
    使用任意数量的关键字实参
    :param first:
    :param last:
    :param user_info:
    :return:
    """
    profile = {'first_name': first, 'last_name': last}

    for key, value in user_info.items():
        profile[key] = value
    return profile


if '__main__' == __name__:
    # test001('dog', 'harry')
    # print('--------------')
    # test001(animal_type='hamster', pet_name='harry')
    # test002('mushrooms', 'green peppers', 'extra cheese')

    user_profile = test003('albert', 'einstein', location='princeton', field='physics')
    print(user_profile)
