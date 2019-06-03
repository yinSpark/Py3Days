# 约瑟夫环算法

# n个人,编号(1,...n),k编号人开始从1报数,数到m出局,下个人再从1开始报数
# 求k值

# 参考
# https://blog.csdn.net/korosue/article/details/86568220
def joseph_ring(n, m):
    L = list(range(1, n+1))
    if n == 1:
        return
    else:
        index_ = 0
        for i in range(n-1):
            index_ = (index_ + m) % len(L) - 1
            print('出局人编号: %d' % L[index_])
            del L[index_]
            if index_ < 0:
                index_ = 0
        # print('余下人编号: %d' % L[0])
        return L[0]

if __name__ == '__main__':

    result = fn(10, 6)
    print('余下人编号: %d' % result)

