import time

library = []


# --- 辅助函数：按书名查找图书 ---
def find_book(title):
    for book in library:
        if book.get('名字') == title:
            return book
    return None


# --- 第一阶段：录入图书 ---
print("=== 图书录入系统 (需录入至少5本) ===")
while True:
    # 录入书名并检查重复
    while True:
        title = input('\nEnter a book title (书名): ').strip()
        if not title:
            print('错误：书名不能为空！')
            continue
        if find_book(title):
            print('错误：该书名已存在！')
            continue
        break

    author = input('Enter a book author (作者): ')
    # 按照你的要求：第三个输入直接作为“状态”
    status = input('Enter book status (初始状态，如“存在”或“已借出”): ')

    book = {
        '名字': title,
        '作者': author,
        '状态': status
    }
    library.append(book)
    print(f"成功添加《{title}》，当前状态为：{status}")

    if len(library) >= 5:
        if input('\n是否继续录入？(y/n): ').lower() == 'n':
            break

# --- 第二阶段：操作系统 ---
menu = """
=======================
    1. 借书 (Borrow)
    2. 还书 (Return)
    3. 查询 (Query)
    4. 显示所有 (All)
    5. 退出 (Exit)
======================="""

while True:
    print(menu)
    result = input('请选择操作: ')

    if result == '1':
        book_title = input('请输入要借阅的书名: ')
        book = find_book(book_title)
        if book:
            # 只有状态为“存在”时才能借
            if book.get('状态') == '存在':
                book['状态'] = '已借出'
                print(f'借阅成功！《{book_title}》状态已改为：已借出')
            else:
                print(f'借阅失败！该书当前状态为：{book.get("状态")}')
        else:
            print(f'不存在图书：{book_title}')

    elif result == '2':
        book_title = input('请输入要归还的书名: ')
        book = find_book(book_title)
        if book:
            # 只有状态为“已借出”时才能还
            if book.get('状态') == '已借出':
                book['状态'] = '存在'
                print(f'归还成功！《{book_title}》状态已改为：存在')
            else:
                print(f'还书失败！该书当前状态为：{book.get("状态")}')
        else:
            print(f'不存在图书：{book_title}')

    elif result == '3':
        book_title = input('请输入要查询的书名: ')
        book = find_book(book_title)
        if book:
            print(f"\n--- 《{book_title}》详细信息 ---")
            for k, v in book.items():
                print(f"{k}: {v}")
        else:
            print(f'不存在图书：{book_title}')

    elif result == '4':
        print(f"\n{'书名':<15} | {'作者':<15} | {'状态':<10}")
        print("-" * 45)
        for book in library:
            print(f"{book['名字']:<15} | {book['作者']:<15} | {book['状态']:<10}")

    elif result == '5':
        print('正在退出，请稍候...')
        time.sleep(2)
        print('已安全退出')
        break

    else:
        print('输入无效，请输入 1-5 之间的数字')