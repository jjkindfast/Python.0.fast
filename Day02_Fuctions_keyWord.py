# 请你定义一个名为 build_hero 的函数，要求：
#
# 1. 第一个参数是 name （英雄名）。
# 2. 第二个参数是 type （职业）。
# 3. 后面的参数用 **kwargs 接收（用来存储额外的属性，如 hp, mp, attack 等）。
# 4. 函数内部先打印英雄基本信息，再遍历打印出所有的额外属性。
# 示例调用： build_hero('鲁班', '射手', hp=3400, skin='电玩小子')
def build_hero(name,type,**kwargs):
    part=[f"{key}:{value}" for key,value in kwargs.items()]
    print("{},{},{}".format(name,type,part))

while True:
    name=input('name:')
    type=input('type:')
    keywords=[]
    key_value={}
    while True:
        keyword=input('keyword:').strip()
        if not keyword:
            break
        keywords.append(keyword)
    for i in keywords:
        # 这里的 i 就是 'a', 'b', 'c' 中的一个
        value = input(f"请输入 {i} 的对应值: ")
        # 核心语法：字典名[键] = 值
        key_value[i] = value
    build_hero(name,type,**key_value)
