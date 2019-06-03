# 算法题目一
# 有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；
# 要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。

# 理论分析
# 1.两个列表合成一个新列表,并求和
# 2.使用排列组合迭代器combinations(list, int(len(list)/2))获取有序不重复的组合
# 3.通过以上组合求得两列表差的绝对值列表,求得最小差值
# 4.再次遍历求得一个最小差值的其中一个列表
# 5.求得另一列表

from itertools import combinations
from random import randint

def random_array(n):
    return [randint(0, 50) for _ in range(n)]

def target_list(a, b):
    c = a + b
    c.sort()
    sum_c = sum(c)
    # print(sum_c, c)
    dif_arr = []
    for i in combinations(c, int(len(c)/2)):
        dif = sum_c - sum(i) * 2
        dif_arr.append(abs(dif))
    dif_arr.sort()
    # print(dif_arr[0])
    for j in combinations(c, int(len(c)/2)):
        if abs(sum_c - sum(j) * 2) <= dif_arr[0]:
            new_a = list(j)
            break
    # print(sum(new_a), new_a)
    for x in new_a:
        c.remove(x)
    # print(sum(c), c)
    new_b = c
    return new_a, new_b


if __name__ == '__main__':
    a, b = random_array(5), random_array(5)
    x, y = target_list(a, b)
    print(sum(x), x)
    print(sum(y), y)

