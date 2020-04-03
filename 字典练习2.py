#按顺序遍历字典中的所有键
favorite_languege = {
	"jen":"python",
	"sarah":"C",
	"edward":"ruby",
	"phil":"python",
}
for name in sorted(favorite_languege.keys()):
	print(name.title() + ", thank you for talking the poll.")
#sorted()按顺序

#遍历字典中的所有值
favorite_languege = {
	"jen":"python",
	"sarah":"C",
	"edward":"ruby",
	"phil":"python",
}
for languege in favorite_languege.values():
	print(languege.title())
#values()加for循环遍历字典中的值，values()是把字典中所有的值都打印，不管相同与否
favorite_languege = {
	"jen":"python",
	"sarah":"C",
	"edward":"ruby",
	"phil":"python",
}
for languege in set(favorite_languege.values()):
	print(languege.title())
#set()函数在favorite_languege.values()中提取出不同的元素，会打印一个无重复值的列表