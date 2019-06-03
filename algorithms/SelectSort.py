# 选择排序算法
# 和插入排序很像

# 算法思想
# 简单的说，就是有一组数，然后从中选择找出最大的一个，把这个数排到第一个或者最后一个，
# 然后找出第二大的数，排到第二个或者倒数第二个，就这样一直到所有数字都排好为止。

# 算法分析
arr = [7, 3, 5, 2, 1, 4]
# 1: 3, 5, 2, 1, 4, 7  找到7
# 2: 3, 2, 1, 4, 5, 7  找到5
# 3: 3, 2, 1, 4, 5, 7  找到4
# 4: 2, 1, 3, 4, 5, 7  找到3
# 5: 1, 2, 3, 4, 5, 7  找到2, 1

# 总结: 循环5次,

# 算法实现
# 每次得到最小值

from random import randint

#  生成一个随机array
def random_array(n):
    '''
    :param n: number
    :return: array
    :description: Generate a random array
    '''
    return [randint(0, 50) for _ in range(n)]

def select_sort(arr):
    times = len(arr)
    for i in range(times - 1):
        # 默认每次循环的第一个值为最小值
        least = i
        for j in range(i + 1, times):
            if arr[j] < arr[least]:
                arr[least], arr[j] = arr[j], arr[least]

        print('第{}次排序结果: {}'.format(i + 1, arr))

    return arr

if __name__ == '__main__':
    arr = random_array(10)
    result = select_sort(arr)
    print('选择排序结果: {}'.format(result))

