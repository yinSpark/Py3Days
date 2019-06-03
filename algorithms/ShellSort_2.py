# 希尔排序算法---使用插入排序

# 算法思想
# 在直接插入排序上的改进,也称缩小增量排序.取增量进行逻辑分组进行直接插入排序

# 算法分析(取增量,使用round()取值更好)
# 第一次增量的取法为： d = count / 2
# 第二次增量的取法为: d = (count / 2) / 2
# 最后一直到: d = 1

# 算法实现
from random import randint

def random_array(n):

    return [randint(0, 50) for _ in range(n)]

def insert_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr

def shell_sort(arr):
    n = len(arr)
    # 获取增量
    inc = round(n/2)
    while inc >= 1:
        for i in range(n):
            min_index = i
            for j in range(i+inc, n, inc):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        print("当增量为{}时排序结果: {}".format(inc, arr))
        inc = round(inc / 2)
    return arr


if __name__ == '__main__':
    arr = random_array(13)
    result = shell_sort(arr)
    print("希尔排序排序结果: {}".format(result))
