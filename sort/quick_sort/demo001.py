"""
供练习使用
"""


def quick_sort(nums, start, end):
    """
    练习1
    :param nums:
    :param start:
    :param end:
    :return:
    """
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

    quick_sort(nums, start, low - 1)
    quick_sort(nums, low + 1, end)


def quick_sort2(array):
    if len(array) < 2:
        return array
    else:
        mid = array[0]
        less = [i for i in array[1:] if i <= mid]
        greater = [i for i in array[1:] if i > mid]
        return quick_sort2(less) + [mid] + quick_sort2(greater)


if '__main__' == __name__:
    nums = [922, 515, 104, 873, 900, 788, 305, 430, 171, 347]
    print('排序前:', nums)
    # quick_sort(nums, 0, 9)
    nums = quick_sort2(nums)
    print("排序后:", nums)
