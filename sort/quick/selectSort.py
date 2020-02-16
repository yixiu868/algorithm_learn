# encoding=utf8
import random

def selectSort(nums):
    # 循环趟数
    for i in range(len(nums) - 1):
        min = i
        # 每趟比较次数
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[min], nums[i] = nums[i], nums[min] # 交换元素位置
    return nums


if __name__ == '__main__':
    nums = []
    for i in range(10):
        nums.append(random.randint(1, 100))
    print(nums)
    print(selectSort(nums))