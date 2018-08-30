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
