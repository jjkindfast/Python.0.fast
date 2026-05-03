#       工坊物品合成,切割列表练习
# 你是一个炼金术师，你的背包里有一排材料。炼金的规则是：当你发现 “铁 (Iron)” 和 “木头 (Wood)” 挨在一起时，你可以把这两个材料合并成一个 “长剑 (Sword)” 。
import time

bag=[]
while True:
    t1=(input("请输入（用空格隔开）: "))
    parts=t1.split()
    print("当前新parts：",parts)
    print("当前旧bag：",bag)
    # count = len(bag)
    # for j in range(count,len(parts)+count):
    #     print(j)
    #     bag.append(parts[j-count])
    bag.extend(parts)
    i=0
    while i < len(bag) - 1:  # 使用 while 循环，因为列表长度会变
        if bag[i] == "Iron" and bag[i + 1] == "Wood" or bag[i+1] == "Iron" and bag[i] == "Wood":  # 注意是 Wood 不是 Word 哦
            # 切下两个位置，填入一个新列表
            bag[i: i + 2] = ["Sword"]
            print("合成成功！")
            # 合成后不需要 i += 1，因为后面的元素已经补位了
        else:
            i += 1

    print("最终背包：", bag)
    end_result = input('是否继续（退出按“N或n”）')
    if end_result.lower() == 'n':
        time.sleep(1)
        print('已退出！')
        break

#1、列表：绕远路了，
#    count = len(bag)
#    for j in range(count,len(parts)+count):
#       print(j)
#       bag.append(parts[j-count])
#这个更快：
#       bag.extend(parts)#最优解决方法
