# encoding=utf8


def shell_sort(lists):
    """
    希尔排序
    希尔排序的关键并不是随便地分组后各自排序，而是将相隔某个”增量“的记录组成一个子序列，实现跳跃式的移动，使得排序的效率提高。希尔排序是一种
    不稳定的排序方法，平均时间复杂度O(nlogn)，最差的情况下的时间复杂度为O(n^s)(1<s<2)，空间复杂度为O(1)。
    :param lists:
    :return:
    """
    count = len(lists)
    step = 2
    group = count // 2
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    # 内部使用插入排序
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group //= step
    return lists


if '__main__' == __name__:
    lists = [3, 4, 2, 8, 9, 5, 1]
    print('排序前序列为')
    for i in lists:
        print(i)

    print('\n排序后结果为')
    for i in shell_sort(lists):
        print(i)
