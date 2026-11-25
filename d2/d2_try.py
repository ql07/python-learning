try:
    n = int(input("输入一个整数："))
    print("一半是", n / 2)
except ValueError:
    print("这不是整数！")
except ZeroDivisionError:
    print("不能除以0")