my_list = [] #建立一个列表
print(my_list,type(my_list)) #打印列表
my_list = [10] #列表中的元素 
print(my_list,type(my_list)) #打印列表，查看my_list这个变量的type类型(会输出为list)
my_list = [10,20,30,40,50] 
print(my_list,type(my_list))
my_list = [10,"hello",True,None,[1,2,3],print]
print(my_list,type(my_list)) #这个输出说明了python列表的元素可以是整数，字符串，甚至是函数
print(my_list[1])
print(len(my_list)) #len函数，获取列表的元素数，从1开始
print(my_list[1].title()) #title函数 使元素首字母大写
my_list[1] = "python" #在my_list这个列表1这个位置修改元素
print(my_list)
my_list.append("python") #append函数来在列表末尾添加新元素
print(my_list)
my_list.insert(0,"hello") #insert函数，可以在列表指定位置插入元素
print(len(my_list))
del my_list[7] #del语句删除列表中元素，需要知道元素的索引
print(my_list)
#pop() 函数是弹出，即删除了列表最后一个元素，并让你可以继续使用这个值
motorcycles = ["honda","yamaha","suzuki"] #列出几个摩托车的品牌
print(motorcycles)
popend_motorcycles = motorcycles.pop() #popend_motorcycles 来存放motorcycles使用pop函数弹出的值
print(motorcycles)
print(popend_motorcycles)
#其实可以使用pop函数来弹出列表任意位置的元素
fist = motorcycles.pop(0) #弹出列表索引为0 即位置是列表第一个的值
print(motorcycles,fist) #这个输出会看见motorcycles列表里只剩yamaha这一个元素，first会打印出honda
#如果要从列表中删除一个元素，而且不再用任何方式使用这个元素，可以用del语句，如果在和删除元素后，还要继续使用，则用pop()函数
#根据值来删除元素使用remove()的方式
motorcycles = ["honda","yamaha","suzuki","ducati"]
print(motorcycles)
motorcycles.remove("ducati") #直接根据值来删除
print(motorcycles)
motorcycles = ["honda","yamaha","suzuki","ducati"]
print(motorcycles)
a = "ducati"
motorcycles.remove(a) #根据变量来删除列表中的元素
print(motorcycles)
#注意remove()只能删除列表中第一个指定的值。如果要删除的值可能在列表中出现多次，就需要用循环来判断是否删除了所有指定值的元素
#目前关于列表，学了添加元素，删除元素，删除元素有del，pop()，remove()，根据不同需求来选择
