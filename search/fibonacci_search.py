# 斐波那契查找算法

def fibonacci_search(lists, key):
    """
    参考：https://www.cnblogs.com/lsqin/p/9342929.html
        https://www.cnblogs.com/maybe2030/p/4715035.html#_label2
    主题：属于二分查找优化算法，性能比二分查找快
    :param lists:
    :param key:
    :return:
    """
    F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
     233, 377, 610, 987, 1597, 2584, 4181, 6765,
     10946, 17711, 28657, 46368]

    low = 0
    high = len(lists) - 1

    k = 0
    while high > F[k] - 1:
        k += 1
    print(k)
    i = high
    while F[k] - 1 > i:
        lists.append(lists[high])
        i += 1
    print(lists)

    # 算法主逻辑
    time = 0
    while low <= high:
        time += 1
        if k < 2:
            mid = low
        else:
            mid = low + F[k-1] - 1
        print("low=%s, mid=%s, high=%s" % (low, mid, high))
        if key < lists[mid]:
            high = mid - 1
            k -= 1
        elif key > lists[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                print("times: %s" % time)
                return mid
            else:
                print("times: %s" % time)
                return high
    print("times: %s" % time)
    return False


if '__main__' == __name__:
    lists = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = fibonacci_search(lists, 444)
    print(result)
