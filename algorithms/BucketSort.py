# 桶排序算法

# 算法思想
# 桶排序也叫计数排序，简单来说，就是将数据集里面所有元素按顺序列举出来，然后统计元素出现的次数。最后按顺序输出数据集里面的元素。

# 算法分析
# 1.申请一个包含所有元素的数组，并初始化。
# 2.遍历原始数据，并计数。
# 3.遍历计数完成后的各个数组元素，输出数据。

# 算法实现

from random import randint


def random_array(n):
    return [randint(0, 5) for _ in range(n)]


def bucket_sort(arr):
    min_ = min(arr)
    # 初始化一个m位包含所有元素的数组
    buckets = [0] * (max(arr) - min_ + 1)
    # 记录每个值出现的次数
    for i in range(len(arr)):
        buckets[arr[i] - min_] += 1

    print(buckets)
    sort_arr = []
    # 遍历,生成有序数组
    for j in range(len(buckets)):
        sort_arr += [min_ + j] * buckets[j]
    return sort_arr


if __name__ == '__main__':
    arr = random_array(10)
    print(arr)
    sort_arr = bucket_sort(arr)
    print(sort_arr)
