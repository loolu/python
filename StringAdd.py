what_he_does = ' plays '
his_instrument = ' guitar '
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro)

#整型和String连接
'''num = 1
string = '1'
print(num + string)'''

#查看变量类型
num = 1
print(type(num))

string = '1'
print(type(string))

#转换变量类型
num = 1
string = '1'
num2 = int(string)
print(num + num2)

#字符串乘法
words = ' words ' * 3
print(words)

#复杂运算字符串
word = 'a loooooong word'
print(len(word))
num = 12
string = 'bang!'
total = string * (len(word) - num)
print(total)

#字符串的分片与索引(字符串截取)
name = 'My name is mike'
print(name[0])
print(name[-4])
print(name[11:14])
print(name[11:15])
print(name[5:])
print(name[:5])

wordone = 'friends'
find_the_evil_in_your_friends = wordone[0]+wordone[2:4]+wordone[-3:-1]
print(find_the_evil_in_your_friends)

#对于url切片
url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]

print(file_name)

#替换手机号号码中的某几位数字
phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
print(hiding_number)

#简单版电话号码联想功能
search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search) + 1 ) + ' to '+ str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search) + 1 ) + ' to '+ str(num_b.find(search) + len(search)) + ' of num_b')

#format字符串为空填写
print('{} a word she can get what she {} for.'.format('With','came'))
print('{preposition} a word she can get what she {verb} for.'.format(preposition = 'With',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('With','came'))

city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)

#函数
def fahrenheit_converter(C):
    fahrenheit = C * 9/5 + 32
    return str(fahrenheit) + 'F'

C2F = fahrenheit_converter(35)
print(C2F)

#定义函数练习题
def weight_exchange(g):
    kg = g / 1000
    return kg

G = weight_exchange(1)
print(G)

#答案
def g2kg(g):
    return str(g/1000) + 'kg'

print(g2kg(2000))

#定义函数求直角三角形斜边长
def triangle_long(a,b):
    c = ((a * a + b * b) * (1/2))
    return c

print(triangle_long(5,5))

#答案
def Pythagorean_theorem(a,b):
    return 'The right triangle third side\'s length is {}'.format((a**2 + b**2)**(1/2))

print(Pythagorean_theorem(3,4))
    

#计算梯形面积(位置参数)
def trapezoid_area(base_up, base_down, height):
    return 1/2 *  (base_up + base_down) * height
#正确写法
print(trapezoid_area(1,2,3))
#正确写法
print(trapezoid_area(height=3, base_down=2, base_up=1))
#错误写法
print(trapezoid_area(height=3, base_down=2,1))
#错误写法
print(trapezoid_area(base_up=1, base_down=2, 3))
#正确写法
print(trapezoid_area(1, 2, height=3))

'''
打印圣诞树
print的可选参数sep(意为每个打印的结果以...分开)的默认值为‘ ’空格,
但是我们将其重新传入‘/n’也就是换行的意思，一句话说，也就是将每个打印的数以换行符号进行分割。
'''
print('  *',' * *','* * *','  |  ',sep = '\n')

#给定参数设定默认值
def trapezoid_area(base_up, base_down, height=3):
    return 1/2 * (base_up + base_down) * height

print(trapezoid_area(1,2))

trapezoid_area(1,2,height=15)


