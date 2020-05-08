# encoding=utf8
import random

def bubbleSort(nums):
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
    print(bubbleSort(nums))