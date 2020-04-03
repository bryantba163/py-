#操作列表
#1) 遍历整个列表
a = ["ss","kobe","gigi"]
for b in a:
	print(b)
#用for循环来打印出a列表中所有元素
#2）创建数值列表
for a in range(1,10):
	print(a) #会打印1，2，3，4，5，6，7，8，9 range()函数生成一串数字
#注意range()函数有差一性，即range(1,5)会打印1，2，3，4  range(1,3)会打印1，2
numbers = list(range(1,10))
print(numbers)
#使用list()函数来将range()打印出的数字转换为一个列表
#range()函数还可以指定步长来生产数字
even_numbers = list(range(0,11,2))
print(even_numbers) #打印从0开始10以内的偶数，从0开始，不断加2，直到达到终值(11)
#range()函数几乎可以创建任何需要的数字集
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
#这段代码，首先创建了一个空列表squares，接下来使用range()函数遍历1-10的值，然后在把当前值的平方储存到临时变量square中，使用append()函数的目的是将循环中的值，逐一的添加到squares列表的末尾
#可以不使用临时变量square
squares = []
for value in range(1,11):
	squares.append(value**2) #不使用square临时变量
print(squares)
#3）数字列表简单的统计计算
digits = [1,2,3,4,5,6,7]
print(digits)
print(min(digits)) #数字列表的最小值
print(max(digits)) #最大值
print(sum(digits)) #值的和
#4）解析列表
#其实就是把for循环语句和创建新的列表的代码合并
squares = [value**2 for value in range(1,11)]
print(squares)