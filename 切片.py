#切片
player = ["eric","james","durant","morant","ove"]
print(player[0:3]) #从索引的0处开始到索引3前一个值，减一性
print(player[1:3]) #从索引1开始到索引3前一个值
#打印列表的切片，输出也是一个列表
print(player[1:]) #未设置切片末尾的索引，是从切片头索引到列表最后一个元素全部打印
print(player[:4]) #未设置切片开头索引，则是从列表第一个元素开始，到切片末尾索引的前一个元素
print(player[-3:]) #同理切片也可以使用负数索引，这个切片会打印列表最后三个元素
#遍历切片
for player in player[:3]:
	print(player) #只遍历了前三个
#复制列表
my_food = ["pizza","cake","milk","coffe"]
food = my_food[:]
print(my_food)
print(food)
#my_food[:] 这个切片不指定索引，从而创建了这个列表的副本，再将这个副本储存在列表food中
my_food = ["pizza","cake","milk","coffe"]
food = my_food[:]
print(my_food)
print(food)
my_food.append("starbucks")
food.append("ice")
print(my_food)
print(food)
#这段代码证明了my_food这个列表与food这个列表是两个不一样的列表
#如果不使用切片的方式
my_food = ["pizza","cake","milk","coffe"]
food = my_food
print(my_food)
print(food)
my_food.append("ice")
food.append("starbucks")
print(my_food)
print(food)
#这段代码证明了如果不使用切片方式，直接等于，解释器会认为是将my_food这个列表，直接赋值给food，那么my_food与food这个两个变量其实指向同一个列表，所以使用my_food.append和food.append这个两个语句添加元素时两个变量指向的列表都会增加一个元素
#所以在复制列表时，最好使用切片的方式