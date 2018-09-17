open("abc.txt",'r')

#捕捉文件未创建的异常
try:
    open("abc.txt",'r')
except FileNotFoundError:
    print("异常了！")

#NameError异常
try:
    open(aa)
except NameError:
    print("这是一个name异常！")

#python中的异常类都继承Exception
try:
    open("abc.txt",'r')
except Exception:
    print("异常了！")


#python2.5异常类的新的基类BaseException。Exception也继承自BaseException
try:
    open("abc.txt",'r')
except BaseException:
    print("异常了！")


#多个异常无法知道具体时哪个异常了
try:
    open("abc.txt",'r')
    open(aa)
except BaseException:
    print("异常了!")

#使用message打印出异常信息
try:
    open("abc.txt",'r')
    open(aa)
except BaseException as msg:
    print(msg)

#try...except与else配合使用
try:
    aa = "异常测试："
    print(aa)
except Exception as msg:
    print(msg)
else:
    print("没有异常！")

#try...except...finally...
try:
    print(aa)
except Exception as e:
    print(e)
finally:
    print("不管是否异常，我都会被执行。")

try:
    aa = "异常测试："
    print(aa)
except Exception as e:
    print(e)
finally:
    print("不管是否异常，我都会被执行。")

#抛出异常
from random import randint
number = randint(1,9)

if number % 2 == 0:
    raise NameError("%d is even" % number)
else:
    raise NameError("%d is odd" % number)
