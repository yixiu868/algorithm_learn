# encoding=utf8
import random
import time


# 插入排序
def insert_sort(arr, step):
    for i in range(step, len(arr)):
        for j in range(i, step - 1, -step):
            if arr[j] < arr[j-step]:
                arr[j], arr[j-step] = arr[j-step], arr[j]
            else:
                break


# 希尔排序
def shell_sort(arr):
    length = len(arr)
    step = 1

    while step < length // 3:
        step = step * 3 + 1

    while step >= 1:
        insert_sort(arr, step)
        step = step // 3


if __name__ == '__main__':
    arr = [random.randint(0, 1000000) for _ in range(5000)]
    print('待排序数组大小:', len(arr))
    start = time.time()
    shell_sort(arr)
    end = time.time()
    print('用时:', (end - start))