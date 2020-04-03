#列表适合存储可变值，储存不可变值的列表叫做元组
dimensions = (200,50) #元组使用圆括号
print(dimensions[0]) #打印元组第一个元素
print(dimensions[1]) #打印元组第二个元素
#dimensions[0] = 250 #元组的元素不能修改，代码会报错

#遍历元组中的元素
dimensions = (200,50)
for dimension in dimensions:
	print(dimension)
#与遍历列表的方法一样

#修改元组的变量
#虽然不能修改元组的元素，但可以给存储元组的变量赋值。
dimensions = (200,50)
print(dimensions)
dimensions = (400,50)
print(dimensions)
#类似于直接重新赋值了