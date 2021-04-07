# encoding=utf8
import random


def bubble_sort(nums):
    """
    冒泡排序
    一种稳定的排序方法，最好的情况下的时间复杂度为O(n), 最坏的情况下时间复杂度为O(n²), 平均情况下的时间复杂度为O(n²). 空间复杂度为O(1)
    :param nums:
    :return:
    """
    i = 1
    while i < len(nums):
        j = i - 1
        while j < len(nums) - 1:
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            j += 1
        i += 1
    return nums


if __name__ == '__main__':
    nums = []
    for i in range(10):
        nums.append(random.randint(1, 100))
    print(nums)
    print('---------------------')
    print(bubble_sort(nums))