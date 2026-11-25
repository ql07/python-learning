import json

def save(contacts, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False)

def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def ask_number():
    total = 0
    while True:
        n = input("请输入整数(q结束)：")
        if n == 'q':
            return total

        try:
            total += int(n)
        except ValueError:
            print("不是数字，请重新输入")
            continue

print(ask_number())
contacts = load("contacts.json")
contacts["娜美"] = "13800000003"  # 内存里添一条
save(contacts, "contacts.json")  # 写回文件
contacts2 = load("contacts.json")  # 重新读一遍验证
print(contacts2["娜美"])  # 能读到 → 闭环成立
