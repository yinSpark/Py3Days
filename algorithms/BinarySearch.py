# 二分查找算法

# 算法思想
# 二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好；
# 其缺点是要求待查表为有序表，且插入删除困难。
# 因此，折半查找方法适用于不经常变动而查找频繁的有序列表。
# 首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，
# 如果两者相等，则查找成功；否则利用中间位置记录将表分成前、后两个子表，
# 如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。
# 重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。

# 算法分析

# 算法实现

from random import randint

def random_array(n):
    '''
    :param n:
    :return list:
    :description : generate a random array
    '''

    return [randint(0, 30) for _ in range(n)]


def binary_search(key, arr):
    '''
    :param key:
    :param arr:
    :return index:
    :description : Binary search
    '''
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = round((low + high) / 2)
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    arr = random_array(10)
    arr.sort()
    print("升序排列后的arr: {}".format(arr))
    key = int(input("请输入一个想查找的整数: "))
    result = binary_search(key, arr)
    if result != -1:
        print("{}在arr的index为: {}".format(key, result))
    else:
        print("在arr中找不到key: {}".format(key))
