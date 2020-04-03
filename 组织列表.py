#使用方法sort()来对列表进行永久排序
car = ["bwm","audi","toyota","subaru"]
print(car)
car.sort() #永久修改了列表元素的排列顺序，按照字母顺序排列的
print(car)
car = ["bwm","audi","toyota","subaru"]
print(car)
car.sort(reverse=True) #对函数sort()传参 reverse=True 来让列表里的元素按照字母顺序相反的顺序来排列
print(car)
#sort() 这种方式对列表排列顺序的改变是永久性的，问题：参数reverse=True为什么可以使元素按照字母顺序相反的顺序
#sorted()对列表临时排序
a = ["b","a","c","h","e"]
print(a)
print("\nsorted后的排序：")
print(sorted(a))  #使用sorted()函数使列表临时排序，仅仅是临时的
print("\n不使用sorted的排序")
print(a)
#这里仅仅是用小写字母做了排序的几个函数的用法，在决定排列顺序时大写字母要指定准确的排列顺序
#倒着打印列表
a = ["a","b","c","d","e"]
print(a)
a.reverse() #reverse()函数，是倒着打印列表是永久性改变列表元素的排列顺序，注意是直接反转列表元素的排列顺序，并不是按照字母顺序的反序了
print(a)
print(len(a)) #用len()函数确认列表元素数时是从1开始的，但是使用列表元素的索引时是从0开始

a = ["bmw","sadh","sas"]
print(a[-1])
print(a[3]) #列表的索引从0开始，但是可以是负数，-1即代表了最后一个元素
