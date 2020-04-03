#检查特殊元素
a = ["a","b","v","c","d"]
for b in a:
	if b == "v":
		print("")
	else:
		print("error")
print(a)
#其实是for和if的嵌套

#确定列表是否是空列表
a = []
if a:
	for b in a:
		print(" ")
	print("error")
else:
	print("ok")
#这是先if语句判断然后for循环列表

#使用多个列表
available_toppings = ["mushrooms","olives","green peppers","pepperoni","pineapple","extra cheese"]
requested_toppings = ["mushrooms","french fries","extra cheese"]
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding" + requested_topping + ".")
	else:
		print("Sorry,we don't have" + requested_topping + ".")
print("\nFinished making your pizza!")