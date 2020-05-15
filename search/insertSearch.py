
# 插值查找算法
def insert_search(lists, key):
    """
    基本思想：基于二分查找算法，将查找点的选择改进为自适应选择，可以提高查找效率，插值插值也属于有序查找
    注意：对于表长较大，而关键字分布又比较均匀的查找表来说，插值查找算法的平均性能比折半查找要好的多，反之，数组中如果分布非常不均匀，那么插值查找未必
        是很合适的选择
    复杂度分析：查找成功或者失败的时间复杂度均为O(log2(log2n))
    :param lists:
    :param key:
    :return:
    """
    low = 0
    high = len(lists) - 1
    times = 0

    while low < high:
        times += 1
        # 计算mid值时插值查找算法核心
        mid = low + int((high - low) * (key - lists[low]) / (lists[high] - lists[low]))
        print("mid=%s, low=%s, high=%s" % (mid, low, high))

        if key < lists[mid]:
            high = mid - 1
        elif key > lists[mid]:
            low = mid + 1
        else:
            print("times: %s" % times)
            return mid

    print("times: %s" % times)
    return False


if __name__ == '__main__':
    lists = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = insert_search(lists, 54)
    print(result)