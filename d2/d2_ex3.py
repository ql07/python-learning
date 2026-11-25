total = 0  # ① 放哪：循环外，累加的账本

while True:  # ② 死循环：主动break才能出去
    text = input("输入整数(q结束): ")
    if text == 'q':
        break# ③ q在这里处理：break

    try:
        total += int(text)  # ④ text转int，加进total
    except ValueError:
        print("不是数字，请重新输入")
        continue # ⑤ 提示"不是数字"后continue
        #    （回到循环开头重新问）

print("总和是", total)  # ⑥ 循环外：只有break才到得了这行
