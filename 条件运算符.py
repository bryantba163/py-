# print('你好') if True else print('Hello')
a = 10
b = 20
# print('a的值比较大') if a > b else print('b的值比较大')
# 获取a和b的较大值
max = a if a > b else b
print(max)
a = 40
b = 20
c = 30
# max = a if a > b and a > c else b if b > c else c #写法太绕不推荐
max = a if (a > b and a > c) else (b if b > c else c)
print(max)

