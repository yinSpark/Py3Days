# 平衡点：假如一个数组中的元素，其前面的部分等于后面的部分，那么这个点的位序就是平衡点
# 比如列表numbers = [1,3,2,4,15,26,4,11,10]; 26前面的总和为25，26后面的总和也是25，26这个点就是平衡点；
# 要求：计算一个列表的平衡点，并返回

arr = [1, 3, 2, 4, 15, 26, 4, 11, 10]

# 方案一.通过lambda和filter进行过滤得出index
ind = filter(lambda i: sum(arr[:i]) == sum(arr[i + 1:]), range(1, len(arr) - 1))
# print(list(ind))
print(arr[list(ind)[0]])

# 方案二.通过循环列表找到i
a = [arr[i] for i in range(1, len(arr) - 1) if sum(arr[:i]) == sum(arr[i + 1:])]
print(a[0])

# 方案三(方案二的解说).平衡点不能是第一个,也不能是最后一个
for i in range(1, len(arr) - 1):
    if sum(arr[:i]) == sum(arr[i + 1:]):
        print(arr[i])

# 方案一的解说
# range(1, len(arr) - 1)除了5为True,其余都为False,可用filter()进行过滤
f = lambda i: sum(arr[:i]) == sum(arr[i+1:])
print(f(5), f(1), f(2))