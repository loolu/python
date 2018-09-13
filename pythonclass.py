#类是有一些系列有共同特征和行为事物的抽象概念的总和
class CocaCola:
    formula = ['caffeine','sugar','water','soda']

#类的实例化
coke_for_me = CocaCola()
coke_for_you = CocaCola()

print(CocaCola.formula)
print(CocaCola.formula)
print(CocaCola.formula)

#类的属性和正常的变量并无区别
for element in coke_for_me.formula:
    print(element)

#实例属性
class CocaCola:
    formula = ['caffeine','sugar','water','soda']

coke_for_China = CocaCola()
coke_for_China.local_logo = '可口可乐'

print(coke_for_China.local_logo)

#实例方法
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self):
        print('Energy!')

coke = CocaCola()
coke.drink()

#类的实例方法更多参数
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self,how_much):

        if how_much == 'a sip':
            print('Cool~')
        elif how_much == 'whole bottle':
            print('Headche!')

ice_coke = CocaCola()
ice_coke.drink('a sip')

#魔术方法_init_()
class CocaCola():
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):
        self.local_logo = '可口可乐'

    def drink(self):
        print('Energy!')

coke = CocaCola()
print(coke.local_logo)

class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def _init_(self):

        for element in self.formula:
            print('Coke has {}!'.format(element))

    def drink(self):
        print('Energy!')

coke = CocaCola()

#
class CocaCola():
    formula = ['caffeine','sugar','water','soda']
    def __init__(self,logo_name):
        self.local_logo = logo_name
    
    def drink(self):
        print('Energy!')

coke = CocaCola('可口可乐')
coke.local_logo

#类的继承
class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]
    def _init_(self,logo_name):
        self.loca_logo = logo_name
    
    def drink(self):
        print('You got {} cal energy!'.format(self.calories))

class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
    ]

coke_a = CaffeineFree('Cocacola_FREE')

coke_a.drink()

#类属性和实例属性

#类属性被重新赋值
class TestA:
    attr = 1
obj_a = TestA()

TestA.attr = 42
print(obj_a.attr)

#实例属性被重新赋值
class TestA:
    attr = 1
obj_a = TestA()
obj_b = TestA()

obj_a.attr = 42

print(obj_b.attr)

class TestA:
    attr = 1
    def _init_(self):
        self.attr = 42

obj_a = TestA()

print(obj_a.attr)

#类的扩展理解
obj1 = 1
obj2 = 'String!'
obj3 = []
obj4 = {}
print(type(obj1),type(obj2),type(obj3),type(obj4))

