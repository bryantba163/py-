name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello，" + full_name.title() + "!"
print(message) #把"Hello，" + full_name.title() + "!" 这个拼串语句赋值到message变量
print("\tPython") #\t 为制表符，起到空格的作用
print("Languages:\nPython\nC\nJava") #\n 作为换行符，起到换行的作用
print("Languages:\n\tPython\n\tC\n\tJava") #\n\t 一起使用使\n\t 后的代码换下一行而且下一行开头添加制表符
favorite_language = 'python '
print(favorite_language) # 这样输出‘python ’后有一个空格，在py终端可以明显看出来
print(favorite_language.rstrip()) #rstrip() 删除末尾空白
favorite_language = ' python '
print(favorite_language) #这个输出在py终端看前后都有空格
print(favorite_language.lstrip()) #lstrip() 可以删除开头空白
print(favorite_language.strip()) #strip() 可以删除两端的空格