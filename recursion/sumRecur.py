def sum(arr):
    """
    求和递归实现
    """
    if 1 == len(arr):
        return arr[0]
    else:
        return arr[len(arr)-1] + sum(arr[0:len(arr)-1])


def sum2(arr):
    total = 0
    for x in arr:
        total += x
    return total


if __name__ == '__main__':
    print(sum([x for x in range(101)]))
    print('--------------------------')
    print(sum2([x for x in range(101)]))