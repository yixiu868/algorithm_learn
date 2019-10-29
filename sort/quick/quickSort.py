import random


# 快速排序
def quick_sort(nums, start, end):
    if start >= end:
        return
    low = start
    mid = nums[start]
    high = end
    while low < high:
        while low < high and mid <= nums[high]:
            high -= 1
        nums[low] = nums[high]
        while low < high and mid > nums[low]:
            low += 1
        nums[high] = nums[low]
    nums[low] = mid
    quick_sort(nums, start, low-1)
    quick_sort(nums, low+1, end)


# 快速排序测试代码
if __name__ == '__main__':
    nums = []
    for i in range(100):
        nums.append(random.randint(1, 1000))
    print('the raw nums is:', nums)
    quick_sort(nums, 0, len(nums)-1)
    print('the sorted nums is:', nums)
