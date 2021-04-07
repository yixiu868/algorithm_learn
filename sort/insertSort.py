# encoding=utf-8

import random


def insert_sort(nums):
    """
    插入排序
    插入排序时一种稳定的排序方法，最好的情况下的时间复杂度为O(n), 最坏的情况下时间复杂度为O(n²), 平均情况下时间复杂度为O(n²). 空间复杂度为O(1)
    :param nums:
    :return:
    """
    # 排序趟数
    for i in range(1, len(nums)):
        current = nums[i]
        pre_index = i - 1
        while pre_index >= 0 and nums[pre_index] > current:
            nums[pre_index+1] = nums[pre_index]
            pre_index -= 1
        nums[pre_index+1] = current
    return nums


def test_arr(count, limit):
    arr = []
    for i in range(count):
        arr.append(random.randint(1, limit))
    return arr


if __name__ == '__main__':
    arr = test_arr(10, 100)
    print('插入排序前:')
    print(arr)
    insert_sort(arr)
    print('插入排序后:')
    print(arr)
