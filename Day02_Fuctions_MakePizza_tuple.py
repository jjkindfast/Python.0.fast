# 请你定义一个名为 make_pizza 的函数，要求：
#
# 1. 第一个参数是 size （尺寸，如 12 ）。
# 2. 后面的参数是 *toppings （配料，数量不限）。
# 3. 函数内部打印出：“正在制作一个 [size] 寸的披萨，配料包括：[所有的配料]”。
# 示例调用： make_pizza(12, '芝士', '培根', '青椒')
def make_pizza_tuple(size,*toppings):
    result=" + ".join([str(i) for i in toppings])
    print("尺寸：{}，配料：{} ".format(size,result))

size=int(input('请输入尺寸：'))
my_list=[]
while True:
    result=input('请输入配料：(输入n或N结束）')
    if result.lower()=='n':
        break
    my_list.append(result)
    toppings=tuple(my_list)
make_pizza_tuple(size,*toppings)
# make_pizza_tuple(size,toppings)

#错误①：类型错误：list.append(result)TypeError: descriptor 'append' for 'list' objects doesn't apply to a 'str' object,list是类名，不可作为变量名
#知识点②：引号里的内容就是 “连接符号” ，你可以换成任何你喜欢的样子：
# 1. 空格隔开 ： " ".join(toppings) [ o bj ec tO bj ec t ] → 芝士 培根 青椒
# 2. 逗号隔开 ： ", ".join(toppings) [ o bj ec tO bj ec t ] → 芝士, 培根, 青椒
# 3. 加号隔开 ： " + ".join(toppings) [ o bj ec tO bj ec t ] → 芝士 + 培根 + 青椒
# 4. 换行隔开 ： "\n".join(toppings) [ o bj ec tO bj ec t ] → 每个配料占一行
#知识点③：总结
# 一、调用时写： make_pizza(size, toppings)
#
# 1. 传入前 ：你手里有一个包裹 ('12', '13') 。
# 2. 进入函数 ： *args 看到你只扔了一个东西过来，不管它是什么，都会强行再给它套一个大纸箱。
# 3. 结果 ： args 变成了 (('12', '13'), ) 。
#    - 老师点评：这就是你说的“在外面再加上一个括号”，导致了数据变成了“嵌套元组”。
# 二、调用时写： make_pizza(size, *toppings)
#
# 1. 传入前（拆箱） ： * 号先发力，把 ('12', '13') 的包装拆掉，让 '12' 和 '13' 变成两个 散装 的参数。
# 2. 进入函数（装箱） ： *args 看到来了两个散客，于是伸出手把它们抓过来，整齐地装进一个新的元组里。
# 3. 结果 ： args 变成了 ('12', '13') 。
#    - 老师点评：这就是你说的“先拆开，传入后再重新包装”。这样得到的元组是干净、扁平的一维元组。
# 三、 在 Python 中，只要一个东西是 “可迭代的（Iterable）” （也就是说它能用 for 循环遍历），它就能被 * 号拆开。
#
# - 列表 ：拆成元素。（能用）
# - 元组 ：拆成元素。（能用）
# - 集合 ：拆成元素。（集合无序，顺序会乱）
# - 字符串 ：拆成字符。
# - 字典 ：拆成键。（会丢失value值）