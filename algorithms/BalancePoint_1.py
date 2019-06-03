# 平衡点：假如一个数组中的元素，其前面的部分等于后面的部分，那么这个点的位序就是平衡点
# 比如列表numbers = [1,3,2,4,15,26,4,11,10];
# 26前面的总和为25，26后面的总和也是25，26这个点就是平衡点；
# 要求：计算一个列表的平衡点，并返回

def balance_point(arr):
    sum_arr = sum(arr)
    balance = 0
    for number in arr:
        if balance < (sum_arr-number)/2:
            balance += number
        else:
            break
    print(balance, number)
    if balance == (sum_arr-number)/2:
        print("存在平衡点: {}".format(number))
    else:
        print("平衡点不存在")

if __name__ == '__main__':
    numbers = [1, 3, 2, 4, 15, 26, 4, 11, 10]
    balance_point(numbers)


