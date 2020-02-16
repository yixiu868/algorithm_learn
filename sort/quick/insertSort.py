# encoding=utf-8

import random

def insert_sort(nums):
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
