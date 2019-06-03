# 希尔排序算法---使用插入排序(推荐)

# 算法思想
# 在直接插入排序上的改进,也称缩小增量排序.取增量进行逻辑分组进行直接插入排序

# 算法分析(取增量,使用round()取值更好)
# 第一次增量的取法为： d = count / 2
# 第二次增量的取法为: d = (count / 2) / 2
# 最后一直到: d = 1

# 算法实现
from random import randint


# 生成长度为n的数组
def random_array(n):
    return [randint(0, 50) for _ in range(n)]


# 进行直接插入排序
def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        if arr[j] > arr[i]:
            arr[j], arr[i] = arr[i], arr[j]

        j = j - 1
        while arr[j] > arr[j + 1] and j >= 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j = j - 1

    return arr


# 进行希尔排序, 直接插入排序(推荐)
def shell_sort(arr):
    n = len(arr)
    # 使用round()设置增量更好,round(1/2)=0,round(2/3)=2
    # 当round()函数在0.5取值时会上偶数取整,可使round(1/2)=0作为退出条件
    inc = round(n / 2)

    while inc >= 1:
        # 0, 0+inc, 0+inc+inc
        for i in range(inc, n):
            # 有序列表最后一位index
            j = i - inc
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
            j = j - inc
            while arr[j] > arr[j + inc] and j >= 0:
                arr[j], arr[j + inc] = arr[j + inc], arr[j]
                j = j - inc
        print("当增量为{}时排序结果: {}".format(inc, arr))
        inc = round(inc / 2)

    return arr


if __name__ == '__main__':
    arr_1 = random_array(10)
    result_1 = insert_sort(arr_1)
    arr_2 = random_array(13)
    result_2 = shell_sort(arr_2)
    print("直接插入排序排列结果: {}".format(result_1))
    print("希尔排序排列结果: {}".format(result_2))
