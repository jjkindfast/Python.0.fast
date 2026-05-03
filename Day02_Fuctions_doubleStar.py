def study_star(*args):
    result=" + ".join([str(i) for i in args])
    print(result)

def study_star2(**args):
    parts = [f"{k}:{v}" for k, v in args.items()]
    result = " - ".join(parts)
    print(result)

args=input('输入：')
study_star(*args)
key=['a','b','c']
key_value={}
for i in key:
    # 这里的 i 就是 'a', 'b', 'c' 中的一个
    value = input(f"请输入 {i} 的对应值: ")
    # 核心语法：字典名[键] = 值
    key_value[i] = value
print('===批量赋值===')
values=[]
for j in range(len(key_value)):
    values.append(input("请输入的对应值: "))
# key_value_p=dict.fromkeys(key,values)
key_value_p = dict(zip(key, values))
study_star2(**key_value)
study_star(*key_value)
study_star2(**key_value_p)


#1、args.items()是字典特有的方法。
#2、列表套字典可实现多个字典
#3、字典赋值：①循环赋值②批量赋值
#4、错误点：values=[]
# for j in range(len(key_value)):
#     values[j]=input(f"请输入的对应值: ")这种情况是导致IndexError: list assignment index out of range
#values是空，但列表values=赋值语句赋值的前提是列表里面得有值。
#5、错误点：key_value_p=dict.fromkeys(key,values)，他是复印机：传入[1,2,3]，这种情况下它会把[1,2,3]给每一个key分一个
#6、错误点：key_value_p = dict(zip(key, values)),它是1对1，传入[1,2,3]则会a对应1，b对应2，c对应3。
#7、如果你在一个函数里想把所有的参数类型都用上，必须遵守这个 唯一的顺序 ：
# 1. 位置参数
# 2. 默认参数
# 3. 可变参数 ( *args )
# 4. 关键字可变参数 ( **kwargs )