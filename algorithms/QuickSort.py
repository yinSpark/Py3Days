# 快速排序算法

# 算法思想
# 先从待排序的数组中找出一个数作为基准数（取第一个数即可），
# 然后将原来的数组划分成两部分：小于基准数的左子数组和大于等于基准数的右子数组。
# 然后对这两个子数组再递归重复上述过程，直到两个子数组的所有数都分别有序。
# 最后返回“左子数组” + “基准数” + “右子数组”，即是最终排序好的数组。

# 算法实现
# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# 语法：list.pop(obj=list[-1])
# 默认为 index=-1，删除最后一个列表值。
# obj -- 可选参数，要移除列表元素的对象。
# 该方法返回从列表中移除的元素对象。

# arr = [12, 30, 5, 16, 5, 1, 20]
# print(a.pop(0))
# print(a)

from random import randint

#  生成一个随机array
def random_array(n):
    '''
    :param n: number
    :return: array
    :description: Generate a random array
    '''
    return [randint(0, 50) for _ in range(n)]

# 进行快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    left, right = [], []
    # 取第一个元素,pop(-1)为默认
    base = arr.pop(0)
    for x in arr:
        if x < base:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [base] + quick_sort(right)

if __name__ == '__main__':
    arr = random_array(10)
    result = quick_sort(arr)
    print(result)




















