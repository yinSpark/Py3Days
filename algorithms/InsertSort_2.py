# 插入排序算法
# 和选择排序很像

# 算法思想

# 算法分析
# 1.设定最小值下标为当前循环i下标
# 2.当前值和后面每一个值比较找到最小值下标
# 3.把当前下标的值设定为找到的最小值
# 经过遍历,每一个当前值都是无序列表的最小值

# 算法实现

from random import randint

def random_array(n):

    return [randint(0, 50) for _ in range(n)]

def insert_sort(arr):
    n = len(arr)
    for i in range(n):
        # 设定有序列表最小值下标
        min_index = i
        # 遍历无序列表, 和有序列表最小值比较,找到无序列表最小值下标,并设定为有序列表最小值下标
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        # 和当前值进行交换
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr

if __name__ == '__main__':
    arr = random_array(10)
    result = insert_sort(arr)
    print(result)
