age = int(input("请输入年龄： "))
if age <= 5:
	print("幼儿园")
elif age <= 10 and age >= 6:
	print("小学生")
elif age <= 18 and age >= 11:
	print("未成年")
else:
	print("成年人")