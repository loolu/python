#使用字符串
#字符串不可改变,不可给元素赋值，也不能切片赋值
website = 'http://www.python.org'
website[-3] = 'com'

#
format = "Hello, %s. %s enough for ya?"
values = ('world', 'hot')
print(format % values)

from string import Template
tmpl = Template("Hello, $who! $what enough for ya?")
print(tmpl.substitute(who='Mars', what='Dusty'))


print("{}, {} and {}".format("first", "second", "third"))
print("{0}, {1} and {2}".format("first", "second", "third"))
print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to"))

from math import pi
print("{name} is approximately {value:.2f}.".format(value=pi, name="π"))
print("{name} is approximately {value}.".format(value=pi, name="π"))

from math import e
print(f"Euler's constant is roughly {e}.")
print("Euler's constant is roughly {e}.".format(e=e))