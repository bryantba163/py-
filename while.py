#while 循环
number = 1
while number <= 5:
	print(number)
	number += 1
#先创建变量number，然后number <= 5，就输出number，然后number = number + 1，循环到number >= 5
#用户输入特定值终止循环
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. " 
message = "" 
while message != 'quit':     
	message = input(prompt)     
	print(message)
	if message != 'quit':
		print(message)