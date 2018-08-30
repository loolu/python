'''
Python中的四种数据结构，分别是：列表、字典、元组，集合
'''
#列表
list = [val1,val2,val3,val4]
#字典
dict = {key1:val1,key2:val2}}
#元组
tuple = (val1,val2,val3,val4)
#集合
set = {val1,val2,val3,val4}

'''
列表

特征：
1.列表中的每一个元素都是可变的
2.列表中的元素是有序的，也就是说每一个元素都有一个位置；
3.列表可以容纳pyhon中的任何对象
'''
#列表的增删改查
fruit = ['pineapple','pear']
fruit.insert(1,'grape')
print(fruit)
#使用insert方法，必须指定在列表中要插入新的元素的位置，插入元素的实际位置是在指定位置之前的位置，
#如果指定插入的位置在列表中不存在，实际上也就是超出指定列表长度，那么这个元素一定会被放在列表的最后位置。

#另外一种插入的方法
fruit[0:0] = ['Orange']
print(fruit)

#删除列表中的元素
fruit.remove('grape')
print(fruit)

#另外一种删除的方法
del fruit[0:2]
print(fruit)

#替换
fruit[0] = 'Grapefruit'
print(fruit)

#列表不能查看某个具体的值所在的位置

'''
字典

特征：
1.字典中数据必须是以键值对的形式出现的
2.逻辑上讲，键是不能重复的，而值可以重复
3.字典中的键(key)是不可变得，也就是无法修改的；而值(value)是可变得，可修改的，可以是任何对象
'''
a = {'key':123,'key':12345}
print(a)

#字典的增删改查
NASDAQ_code = {'BIDU':'Baidu','SINA':'Sina'}

#单一增加
NASDAQ_code['YOKU'] = 'Youku'
print(NASDAQ_code)

#多个增加
NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})
print(NASDAQ_code)

#删除
del NASDAQ_code['FB']
print(NASDAQ_code)

#通过键索引值
NASDAQ_code['TSLA']

#字典不能够切片
chart[1:4]


'''
元组(tuple)
元组可以理解成一个稳固版的列表，因为元组是不可修改的，因此在列表中存在的方法均不可使用在元组上，
但是元组是可以被查看索引的，方式就和列表一样
'''

letters = ('a','b','c','d','e','f','g')
letters[0]

'''
集合(Set)
每一个集合中的元素是无序的、不重复的任意对象
'''
a_set = {1,2,3,4}

#添加
a_set.add(5)
print(a_set)

#删除
a_set.discard(5)
print(a_set)


#数据结构的一些技巧
num_list =[6,2,7,4,1,3,5]
print(sorted(num_list))

sorted(num_list,reverse=True)



