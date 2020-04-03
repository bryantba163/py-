#用户输入input()函数
message = input("请输入： ")
print(message)
#input的注意点就是应该准确指出用户提供的输入内容
name = input("Enter your name： ")
print(name)
#当input的提示内容过多时，也可以把提示赋值给变量
a = "If you tell us who you are, we can send the messages to you."
a += "\nwhat is your name? PLEASE ENTER: "
name = input(a)
print("\nhello, " + name + "!")
#把input的提示放到变量a中

#使用int()来获取数值输入
age = int(input("请输入你的年龄： "))
#input输入的是一个字符串，使用int转换为整型
if age >= 18:
	print("llll")
elif age < 18:
	print("2222")
#在实际的程序中int使用的场景：
height = int(input("How tall are you, in inches?"))
if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

#求模运算% 4%3返回4除以3的余数
#典型例子测试一个数的奇偶性
number = int(input("Enter a number, and I'll tell you if it's even or odd： "))
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")