year = int(input("输入一个年份： ")) #创建一个变量来储存用户输入的年份
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: #条件判断语句来判断是否对4整除and不能被100整除or可以被400整除
	print("是闰年")
else:
	print("不是闰年")