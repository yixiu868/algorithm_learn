# encoding=utf8
import random


def select_sort(nums):
    """
    选择排序：
    是一种不稳定的排序方法，最好、最坏和平均情况下的时间复杂度都为O(n²), 空间复杂度为O(1)
    :param nums:
    :return:
    """
    for i in range(len(nums) - 1):
        min = i
        # 每趟比较次数
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[min], nums[i] = nums[i], nums[min]  # 交换元素位置
    return nums


if __name__ == '__main__':
    nums = []
    for i in range(10):
        nums.append(random.randint(1, 100))
    print(nums)
    print(select_sort(nums))