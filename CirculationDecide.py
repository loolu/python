print(True > False)

#列表
album = []

album = ['Black Star','David Bowie',25,True]

album.append('new song')

print(album)

#打印列表中的第一个和最后一个元素
print(album[0],album[-1])

print('Black Star' in album)

the_Eddie = 'Eddie'
name = 'Eddie'
print(the_Eddie == name)
print(the_Eddie is name)

#bool函数
print(bool(0))
print(bool([]))
print(bool(''))
print(bool(False))
print(bool(None))

#Boolean Operators
print(1 < 3 and 2 < 5)
print(1 < 3 and 2 > 5)
print(1 < 3 or 2 > 5)
print(1 < 3 and 2 > 5)

#条件控制
def account_login():
    password = input('Password:')
    if password == '12345':
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()
account_login()

#条件控制，重置密码
password_list = ['*#*#','12345']
def account_login():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()
account_login()

print(password_list)


#循环(Loop)
for every_letter in 'Hello world':
    print(every_letter)

for num in range(1,11):#不包含11，实际范围是1~10
    print(str(num) + ' + 1 =',num + 1)

songslist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print(song,' - Dio')
    elif song == 'Thunderstruck':
        print(song,' - AC/DC')
    elif song == 'Rebel Rebel':
        print(song,' - David Bowie')


#嵌套循环
for i in range(1,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))


#while循环
while 1 < 3:
    print('1 is smaller than 3')

count = 0
while True:
    print('Repeat this line !')
    count = count +1
    if count == 5:
        break


#条件控制，重置密码加入while循环
password_list = ['*#*#','12345']

def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]
        if password_correct:
            print('Login success!')

        elif password_reset:
            new_password = input('Enter a new password:')
            password_list.append(new_password)
            print('Password has changed succeesfully!')
            account_login()

        else:
            print('Wrong password or invalid input!')
            tries = tries - 1
            print( tries, 'times left')

    else:
        print('Your account has been suspended')

account_login()


#复利函数
'''def invest(amount,rate,time):
    times = 1
    while times <= time:
        print('principal amount:'+ str(amount)
        print('year ' + str(times) + ': $')
        times = times + 1

invest(100,5,8)

 + str(amount+(amount*(rate/100)))
'''

 #答案
 def invest(amount,rate,time):
     print('princical amount: {}'.format(amount))
     for t in range(1, time + 1):
         amount = amount * (rate + 1)
         print('year {}: {}'.format(t,amount))

invest(100, 0.05, 8)

#打印1~100内的偶数
for i in range(1,101):
    if i % 2 == 0:
        print(i)

#sum函数
a_list = [1,2,3]
print(sum(a_list))


import random

point1 = random.randrange(1,7)
point2 = random.randrange(1,7)
point3 = random.randrange(1,7)

print(point1,point2,point3)

#摇骰子函数
import random

def roll_dice(numbers=3,points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game():
    your_money = 1000
    while your_money > 0:
        print('<<<<< GAME STARTS! >>>>>')
        choices = ['Big','Small']
        your_choice = input('Big or Small :')

        if your_choice in choices:
            your_bet = int(input('How much you wanna bet? - '))
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if youWin:
                print('The points are',points,'You win !')
                print('You gained {},you have {} now'.format(your_bet,your_money + your_bet))
                your_money = your_money + your_bet
            else:
                print('The points are',points,'You lose !')
                print('You lost {},you have {} now'.format(your_bet,your_money - your_bet))
                your_money = your_money - your_bet
        else:
            print('Invalid Words')
    else:
        print('GAME OVER')

start_game()

'''
检查手机号码是哪个运营商
在程序中，常常有一些无线循环的情况，比如当一个程序没有异常发生的时候，让循环一直执行。这时候就需要用到while(True)...break这种用法
如果你使用了 if first_three or first_four in CN_mobile:会一直得到CN_mobile的结果，这是因为在布尔运算中 130 or 1301 会为True
'''
def number_test():

    while True:
        number = input('Enter your number :')
        CN_mobile = [134,135,136,137,150,151,152,158,159,182,183,184,187,188,147,178,1705]
        CN_union = [130,131,132,155,156,185,186,145,176,1709]
        CN_telecom = [133,153,180,181,189,177,1700]
        first_three = int(number[0:3])
        first_four = int(number[0:4])

        if len(number) == 11:

            if first_three in CN_mobile or first_four in CN_mobile:
                print('Operator : China Mobile')
                print('We\'re sending verification code via text to your phone',number)
                break
            elif first_three in CN_union or first_four in CN_union:
                print('Operator : China Union')
                print('We\'re sending verification code via text to your phone',number)
                break
            elif first_three in CN_telecom or first_four in CN_telecom:
                print('Operator : China Telecom')
                print('We\'re sending verification code via text to your phone',number)
                break
            else:
                print('No such a operator')
        else:
            print('Invalid length,your number should be in 11 digits')

number_test()
    
