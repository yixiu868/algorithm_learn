# 二分查找算法

# 二分查找，前提是查询list是有序的

def binary_search(data_list, target):
    """
    data_list: 传入的有序列表
    target: 要查找的目标值
    """
    low = 0  # 下标最小值
    high = len(data_list) - 1  # 下标最大值
    index = 1  # 用来标价查找次数

    while low <= high:
        mid = (low + high) // 2  # 整除，取中间值

        if data_list[mid] == target:
            return "一共查找了%d次, 此数值在列表的下标:%d" % (index, mid)
        elif data_list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

        index += 1
    return "一共找了%d次, 找不到这样的值!" % index


if '__main__' == __name__:
    # ret1 = binary_search(list(range(1, 1000)), 888)
    # ret2 = binary_search(list(range(1, 1000)), 1000)
    # print(ret1)
    # print(ret2)
    lists = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    ret = binary_search(lists, 444)
    print(ret)
