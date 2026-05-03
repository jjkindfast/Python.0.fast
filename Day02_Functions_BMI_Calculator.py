def get_bmi(weight, height):
    return weight / (height * height)


print(get_bmi(weight=90, height=100))
print(get_bmi(90, height=100))
print(get_bmi(90, 100))
#   ①print(get_bmi(weight=90, 100))是↓
# #报错：SyntaxError: positional argument follows keyword argument，位置参数不可在关键字参数后，系统无法知道后面没有关键字的参数传给谁，只能“位置参数先，关键字参数后”

#   ②print(get_bmi(a=90, b=100))
#关键字错误：TypeError: get_bmi() got an unexpected keyword argument 'a'，并没指定a这一关键字，
# 在使用 关键字参数 时，有一个硬性要求： 你写的“键（Key）”的名字，必须和函数定义时的“参数名”一模一样。

#   ③总结：关键字参数
#   好处：你可以不按顺序传参，只要名字对就行。，
#   限制 ：名字 必须 匹配，一个字母都不能错（包括大小写）。