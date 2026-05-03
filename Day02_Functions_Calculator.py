# 项目需求：智能计算器 (Smart Calculator)
# 1. 功能要求： 你分别需要定义 4 个函数，每个函数负责一个数学运算：
#
# add(a, b)：返回两个数的和。
# subtract(a, b)：返回两个数的差。
# multiply(a, b)：返回两个数的积。
# divide(a, b)：返回两个数的商（注意：需要考虑除数为 0 的情况）。
# 2. 逻辑流程：
#
# 程序启动后进入死循环，直到用户选择退出。
# 用户输入操作选项（1/2/3/4/5）。
# 用户输入两个数字。
# 根据选项调用对应的函数，并拿到返回值。
# 使用老师提供的 print 语句显示结果。
import time


def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b == 0:
        #在python中建议使用None,因为if None永远是False
        return None
    return a/b

# def power(a, b=2):
#     return a ** b,平方数公式
def exp(a,b=2):
    result = 1
    for i in range(b):
        result *= a  # 每次都乘以最初的那个 a
    return result



while True:
    print("\n" + "=" * 20)
    print("   简易计算器 v1.0")
    print("=" * 20)
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 平方数 (^)")
    print("6. 指数数 (^)")
    print("0. 退出程序")
    print("=" * 20)
    result=int(input("Enter your choice: "))
    if result == 1:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print('{} + {} = {}'.format(a,b,add(a,b)))
        result=input("按任意按钮继续... ")
    elif result == 2:
        a=int(input("Enter 被减数 number: "))
        b=int(input("Enter 减数 number: "))
        print('{} - {} = {}'.format(a,b,subtract(a,b)))
        result=input("按任意按钮继续... ")

    elif result == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print('{} × {} = {}'.format(a, b, multiply(a, b)))
        result=input("按任意按钮继续... ")

    elif result == 4:
        while True:
            a = int(input("Enter 被除数 number: "))
            b = int(input("Enter 除数 number: "))
            #if not divide(a,b).isalnum():#错因是：isalnum是字符串的内置函数，而如果返回的是int和float是没有这个内置函数的
            #return True,if divide(a,b):#错因是：divide返回了一个非0值，在if判断下也会视为真，进而会进入if里面。
            if divide(a,b) is None:
                print("错误：除数不能为零，请重新输入！")
            else:
                print('{} ÷ {} = {}'.format(a, b, divide(a, b)))
                break
        result=input("按任意按钮继续... ")

    elif result == 5:
        a = int(input("请输入底数: "))
        print('{} ^ 2 = {}'.format(a, exp(a)))
        result=input("按任意按钮继续... ")

    elif result == 6:
        a = int(input("请输入底数: "))
        b = int(input("请输入指数: "))
        print('{} ^ {} = {}'.format(a, b,exp(a,b)))
        result=input("按任意按钮继续... ")


    elif result == 0:
        print("退出程序中...")
        time.sleep(2)
        print("成功退出！")
        break
    else:
        print("输入有误，请输入 1-5 之间的选项。")
        result = input("按任意按钮继续... ")


#  总结：位置参数和默认参数
#   位置参数：加减乘除
#       1、在 Python 中，有三个特殊的值(True、False、None）建议永远使用 is 来比较：
#       2、return True,if divide(a,b):#错因是：divide返回了一个非0值，在if判断下也会视为真，进而会进入if里面。
#       3、if None 永远是 False
#   默认参数：平方、指数
#       1、a**b=a的b次方
