# 求2个列表交集和并集

b1 = [1, 2, 3]
b2 = [2, 3, 4]

x, y = set(b1), set(b2)
print(x | y) # 并集
print(x & y) # 交集
print(x - y) # 差集
print(y - x) # 差集
print(x ^ y) # 对称差集
print(y ^ x) # 对称差集


t = set(['a', 'b', 'c'])
print(t)
t.add('d')
print(t)
t.update(['x', 'y', 'z'])
print(t)
t.remove('a')
print(t)
print(len(t))