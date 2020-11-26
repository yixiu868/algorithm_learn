# 选择排序算法图解实现方式

def findSmallest(arr):
    """
    查找出列表最小元素索引
    :param arr:
    :return:
    """
    # 存储最小的值
    smallest = arr[0]
    # 存储最小元素的索引
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """
    选择排序实现
    :param arr:
    :return:
    """
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if '__main__' == __name__:
    arr = [0, 2, 1, 5, 3, 6, 4, 2, -1]
    print(selectionSort(arr))
