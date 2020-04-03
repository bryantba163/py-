#字典列表
alien_0 = {"color":"green","points":5}
alien_1 = {"color":"yellow","points":10}
alien_2 = {"color":"red","points":15}
aliens = [alien_0,alien_1,alien_2]
print(aliens)#这样打印的不好看
for alien in aliens: #这种方式打印好看
	print(alien)

#外星人不止三个，且每个外星人都是使用代码自动生成的。在下面的示例中，我们使用range()生成了30个外星人
aliens = [] #创建一个存放外星人的空列表
#创建30个绿色的外星人
for alien_number in range(30):
	new_alien = {"color":"green","points":5,"speed":"slow"}
	aliens.append(new_alien)

#显示前五个外星人
for alien in aliens[:5]:
	print(alien)
print("...")
#显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))

#批量来更改外星人的颜色和移动速度，用for和if语句
#创建一个空列表，用于存放外星人
aliens = []
#创建30个绿色外星人
for alien_number in range(0,30):
	new_alien = {"color":"green","points":5,"speed":"slow"}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien["color"] == "green":
		alien["color"] = "yellow"
		alien["points"] = 10
		alien["speed"] = "medium"
	elif alien["color"] == "yellow":
		alien["color"] = "red"
		alien["speed"] = "fast"
		alien["points"] = "15"
for alien in aliens[0:5]:
	print(alien)
print("...")
#这几段代码主要体现了把字典存储在列表里

#下面几段代码显示了将列表存储在字典
#还是披萨的场景
pizza = {
	"crust":"thick",
	"toppings":["mushrooms","extra cheese"],
}
#存储所点pizza的信息
print("You ordered a " + pizza["crust"] + "-crust pizza" + 
	"with the following toppings:")
for topping in pizza["toppings"]:
	print("\t" + topping)
#toppings键与其关联的值是一个列表，存储了顾客要求添加的所有配料
#然后在54行代码中使用topping键，提取了字典中对应的值
#当需要字典中的键关联多个值时，可以在字典中嵌套一个列表
#示例代码：
favorite_language = {
	"a":["python","C"],
	"b":["java"],
	"e":["perl","ruby"],
	"f":["python","go"],
}
for name, languages in favorite_language.items():
	print("\n" + name.title() + "'s favorite language are: ")
	for language in languages:
		print("\t" + language.title())
#这里在字典中的键关联的值是列表，使用items()函数遍历favorit_language字典
#在把关联的键-值对，赋给name，languages变量，这里的languages的赋值其实是列表
#再使用langua变量打印出变量languages的值，注意这里的languages变量一定记住是列表

#字典中嵌套字典
#例子：如果有多个网站用户， 每个都有独特的用户名，可在字典中将用户名作为键，然后将每位用户的信息存储在一个字典中， 并将该字典作为与用户名相关联的值
users = {
	"aeinstenin":{
	"first":"albert",
	"last":"einstein",
	"live":"los angel",
	},
	"mcurie":{
	"first":"marie",
	"last":"einstein",
	"live":"paris",
	},
}
#在字典中嵌套字典
for username,user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info["first"] + " " + user_info["last"]
	live = user_info["live"]
	print("\tFull name: " + full_name.title())
	print("\tLive: " + live.title())
#先创建users的字典，这个字典里的两个键值对，aeinstein和mcurie这两个键分别关联了两个字典
#89行遍历字典users，并依次将每个键存储在变量username中，然后依次将于当前键关联的字典存储在user_info
#90行打印出username
#91行开始访问内部字典。变量user_info包含用户信息字典，而变量user_info这个变量包含的字典里有三个键
#分别为first，last，live，然后full_name输出用户的first和last
#这里要注意的是，在字典嵌套字典时表示每位用户的字典的结构都相同，虽然Python并没有这样的要求，但这使得嵌 套的字典处理起来更容易。倘若表示每位用户的字典都包含不同的键，for循环内部的代码将 更复杂。 
