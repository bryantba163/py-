#添加一对键-值
alient_0 = {"color" : "green","points" : 5}
print(alient_0)
alient_0["x_ponsition"] = 0
alient_0["y_ponsition"] = 25
print(alient_0)
#在字典末尾用方括号加键，然后赋值值

#空字典
alient_0 = {}
print(alient_0)
#再往字典里添加键-值
alient_0 = {}
alient_0["color"] = "green"
alient_0["points"] = 5
print(alient_0)
#修改字典里的值
alient_0 = {"color":"green"}
print("The alient is " + alient_0["color"] + ".")
alient_0["color"] = "yellow"
print("The alient is " + alient_0["color"] + ".")
#就直接像添加字典的值一样改就完事

#来个长点的代码
alient_0 = {"x_ponsition":0,"y_ponsition":25,"speed":"medium"}
print("Original x_ponsition: " + str(alient_0["x_ponsition"]))

#向右移动外星人
#根据外星人的当前速度决定将其移动多远
if alient_0["speed"] == "slow":
	x_increment = 1
elif alient_0["speed"] == "medium":
	x_increment = 2
else:
	#这个外星人的速度很快
	x_increment = 3
#新位置等于老位置加上增量
alient_0["x_ponsition"] = alient_0["x_ponsition"] + x_increment
print("New x_ponsition: " + str(alient_0["x_ponsition"]))
#首先定义了一个外星人，其中包括了初始的x坐标和y坐标，还有速度"medium"
#在第30行代码处，使用if-elif-else结构来确认外星人应该向右移动多远，并将这个值储存在x_increment
#如果外星人的速度为"slow",它将向右移动一个单位，如果"speed" == "medium"则向右移动两个单位
#确定移动变量再其与x_position的当前值相加，关联到字典中的键x_position

#删除键-值对
alient_0 = {"color":"green","points":5}
print(alient_0)
del alient_0["points"]
print(alient_0)
#del永久性删除键-值对

#由类似对象组成的字典
favorite_languege = {
	"jen":"python",
	"sarah":"C",
	"edward":"ruby",
	"phil":"python",
}
#长字典是可以这样多行书写的，最后一个键-值对，加逗号为以后在下一行添加键-值对做准备
print("sarah's favorite languege is " 
	+ favorite_languege["sarah"].title() 
	+ ".")
#print时也可以多好，注意缩进

#遍历字典
user_0 = {
	"username": "efermi",
	"first": "enrico",
	"last": "fermi",
}
for key,value in user_0.items():
	print("\nKEY: " + key)
	print("value: " + value)
#也是用for循环来遍历字典，items()函数来返回字典的键和值
#python中键-值对的返回顺序和存储顺序是不同的，但是python不关心键-值对的存储顺序，只跟踪键和值之间的关联关系
favorite_languege = {
	"jen":"python",
	"sarah":"C",
	"edward":"ruby",
	"phil":"python",
}
for name,languege in favorite_languege.items():
	print(name.title() + "'s favorite languege is " + languege.title() + ".")

#遍历字典中所有的键
favorite_languege = {
	"jen":"python",
	"sarah":"C",
	"edward":"ruby",
	"phil":"python",
}
for name in favorite_languege.keys():
	print(name.title())
#keys()方法遍历字典的键

#直接上代码
favorite_languege = {
	"jen":"python",
	"sarah":"C",
	"edward":"ruby",
	"phil":"python",
}
friends = ["phil","sarah"]
for name in favorite_languege.keys():
	if name in friends:
		print(" Hi" + name.title() + " , I see your favorite languege is " + 
			favorite_languege[name].title() + "!")
#首先创建一个列表friends，存放两个字典里的值，再通过for循环遍历字典中的键，if name这个键in friends这个列表，则打印。。。
#篇幅过长，换个文件继续写