
# 插值查找算法
def insert_search(lists, key):
    low = 0
    high = len(lists) - 1
    times = 0

    while low < high:
        times += 1
        # 计算mid值时插值查找算法核心
        mid = low + int((high - low) * (key - lists[low]) / (lists[high] - lists[low]))
        print("mid=%s, low=%s, high=%s" % (mid, low, high))

        if key < lists[mid]:
            high = mid - 1
        elif key > lists[mid]:
            low = mid + 1
        else:
            print("times: %s" % times)
            return mid

    print("times: %s" % times)
    return False


if __name__ == '__main__':
    lists = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = insert_search(lists, 54)
    print(result)