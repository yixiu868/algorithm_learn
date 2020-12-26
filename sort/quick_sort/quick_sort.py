# encoding: utf-8


def quick_sort(array):
    """
    算法图解实现快速排序
    :param array:
    :return:
    """
    if len(array) < 2:
        # 基准条件：为空或只包含一个元素的数组是“有序”的
        return array
    else:
        # 递归条件
        pivot = array[0]
        # 由所有小于基准值的元素组成的子数组
        less = [i for i in array[1:] if i <= pivot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if '__main__' == __name__:
    print(quick_sort([10, 5, 2, 3]))
