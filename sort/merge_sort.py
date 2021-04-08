# encoding:utf-8


"""
归并排序说明：
二路归并排序的过程需要进行logn次。每一趟归并排序的操作，就是将两个有序子序列进行归并，而每一对有序子序列归并时，记录的比较次数均小于记录的
移动次数，记录的移动次数均等于文件记录的个数n，即每一趟归并的时间复杂度为O(n)。因此二路归并排序在最好、最坏和平均情况的时间复杂度为O(nlogn)，
而且是一种稳定的排序方法，空间复杂度为O(1)。
"""


def merge(left, right):
    """
    归并
    :param left:
    :param right:
    :return:
    """
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    """
    排序
    :param lists:
    :return:
    """
    if len(lists) <= 1:
        return lists

    half_size = len(lists) // 2
    left = merge_sort(lists[:half_size])
    right = merge_sort(lists[half_size:])
    return merge(left, right)


if '__main__' == __name__:
    lists = [3, 4, 2, 8, 9, 11, 2, 1]
    print('排序前序列值:')
    for i in lists:
        print(i)

    print('---------------')
    print('排序后序列值:')
    for i in merge_sort(lists):
        print(i)
