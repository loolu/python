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

#推导式
a = []
for i in range(1,11):
    a.append(i)
print(a)

#列表解析
b = [i for i in range(1,11)]
print(b)

#时间对比
import time

a= []
t0 = time.clock()
for i in range(1,20000):
    a.append(i)
print(time.clock() - t0, "seconds process time")

t0 = time.clock()
b = [i for i in range(1,20000)]
print(time.clock() - t0, "seconds process time")a= []

#列表推导式
list = [item for item in iterable]`

a = [i**2 for i in range(1,10)]
print(a)

c = [j+1 for j in range(1,10)]
print(c)

k = [n for n in range(1,11) if n % 2 ==0]
print(k)

z = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
print(z)

#字典推导式
d = {i:i+1 for i in range(4)}
print(d)

g = {i:j for i,j in zip(range(1,6),'abcde')}
print(g)

g = {i:j.upper() for i,j in zip(range(1,6),'abcde')}
print(g)

#循环列表时获取元素的索引
letters = ['a','b','c']
for num,letters in enumerate(letters):
    print(letters,'is',num + 1)

lyric = 'The night begin to shine, the night begin to shine'
words = lyric.split()
print(words)


'''
列表和元组
通用的序列操作
'''
#索引
greeting = 'hello'
#索引0指向第一个元素
print(greeting[0])
#使用负数索引，python将从右(即从最后一个元素)开始往左数，因此-1是最后一个元素的位置
print(greeting[-1])

#不赋值
print('hello'[0])

#调用函数返回一个序列，可直接对其进行索引操作
fourth = input('year: ')[3]
print(fourth)




#索引操作示例：将以数制定年，月，日的日期打印出来
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#一个列表，其中包含数1~31对应的结尾
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']

#把列表的数据循环打印出来       
for ending in endings:
    print(ending)

#获取用户输入内容
year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

#月和日减1，得到正确的索引
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]


print(month_name + ' ' + ordinal + ',' + year)


#切片
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
print(tag[32:-4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])
print(numbers[7:10])
print(numbers[-3:-1])

#第一个索引指定的元素位于第二个索引指定的元素后面，结果为空序列
print(numbers[-3:0])

#如果切片结束于序列末尾，可省略第二个索引
print(numbers[-3:])

#如果切片始于序列开头，可省略第一个索引
print(numbers[:3])

#复制整个序列
print(numbers[:])

#提取域名
url = input('Please enter the URL:')
domain = url[11:-4]
print("Domain name: " + domain)

#更大的步长
print(numbers[0:10:1])
print(numbers[0:10:2])
print(numbers[::4])

#步长为负数
print(numbers[8:3:-1])
print(numbers[10:0:-2])
print(numbers[0:10:-2])
print(numbers[::-2])
print(numbers[5::-2])
print(numbers[:5:-2])


'''
第一个索引依然包含在内，而第二个索引不包含在内。步长为负数时，第一个索引必须比
第二个索引大。当省略起始和结束索引时，python执行了正确的操作：步长为正数时，它
从起点移到终点，而步长为负数时，它从终点移到起点。
'''

#序列相加