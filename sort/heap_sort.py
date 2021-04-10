# encoding=utf8

# 堆排序讲解：https://blog.csdn.net/minxihou/article/details/51850001
# 堆可以分为大根堆和小根堆，这里用最大堆的情况来定义操作：
# （1）最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点。这是核心步骤，在建堆和堆排序都会用到。比较i的根节点与其所对应i的孩子节点
# 的值。当i根节点的值比左孩子节点的值要小的时候，就把i根节点和左孩子节点所对应的值交换，当i根节点的值比右孩子的节点所对应的值要小的时候，就
# 把i根节点和右孩子节点所对应的值交换。然后再调用堆调整这个过程，可见这是一个递归的过程。
# （2）建立最大堆：将堆所有数据重新排序。建堆的过程其实就是不断做最大堆调整的过程，从len/2开始调整，一直比到第一个节点。
# （3）堆排序：移除位在第一个数据的根节点，并做最大堆调整的递归运算。堆排序是利用建堆和堆调整来进行的。首先先建堆，然后将堆的根节点选出与最
# 后一个节点进行交换，然后将前面len-1个节点继续做堆调整的过程。直到将所有的节点取出，对于n个数我们只需要做n-1次操作。

# 堆排序方法对记录较少的文件效果一般，但对于记录较多的文件还是很有效的，其运行时间主要耗费在创建堆和反复调整堆上。堆排序即使在最坏的情况下，
# 其时间复杂度也是O(nlogn)，它是一种不稳定的排序方法。


def adjust_heap(lists, i, size):
    """
    调整堆，选出最大值索引
    :param lists:
    :param i:
    :param size:
    :return:
    """
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    maxs = i

    if i < size / 2:
        if lchild < size and lists[lchild] > lists[maxs]:
            maxs = lchild
        if rchild < size and lists[rchild] > lists[maxs]:
            maxs = rchild
        if maxs != i:
            lists[maxs], lists[i] = lists[i], lists[maxs]
            adjust_heap(lists, maxs, size)


def build_heap(lists, size):
    for i in range(0, size // 2)[::-1]:
        adjust_heap(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)

    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)


if '__main__' == __name__:
    lists = [3, 4, 2, 8, 9, 5, 1]
    print('排序前序列为')
    for i in lists:
        print(i)

    print('排序后序列为')
    heap_sort(lists)
    for i in lists:
        print(i)
