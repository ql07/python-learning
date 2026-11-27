import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "contacts.json")

def confirm(prompt):
    while True:
        sure = input(prompt)
        if sure.lower() == 'y':
            return True
        elif sure.lower() == 'n':
            return False
        else:
            print("请重新输入！")

def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def load_contacts():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def add_contact(contacts):
    name = input("请输入姓名：")
    if not name:
        print("姓名不能为空")
        return
    if name in contacts:
        print("⚠️", name, "已存在，当前电话：", contacts[name])
        if confirm("是否覆盖(y/n)"):
            contacts[name] = input("请输入电话：")
        else:
            print("已取消")
    else:
        phone = input("请输入电话：")
        contacts[name] = phone

def show_contacts(contacts):
    if not contacts:
        print("通讯录是空的")
    else:
        for k, v in contacts.items():
            print(k, "-", v)

def delete_contact(contacts):
    deletes = input("请输入要删人的姓名：")
    if deletes in contacts:
        del contacts[deletes]
    else:
        print("未找到联系人姓名")

def select_contact(contacts):
    selects = input("请输入查询人姓名：")
    found = False
    for k, v in contacts.items():
        if selects in k:
            found = True
            print(k, '-', v)
    if not found:
        print("未找到联系人")

def modify_contact(contacts):
    name = input("请输入要修改人的姓名：")
    if name in contacts:
        print(name, ",当前电话：", contacts[name])
        if confirm("是否修改(y/n)"):
            contacts[name] = input("请输入新电话号码：")
        else:
            print("已取消")
    else:
        print("未找到联系人")

contacts = load_contacts()

while True:
    print("---------1、添加----------")
    print("---------2、查看----------")
    print("---------3、删除----------")
    print("---------4、查询----------")
    print("---------5、修改----------")
    print("---------0、退出----------")
    choice = input("输入你的选择:")
    if choice == '1':
        add_contact(contacts)
    elif choice == '2':
        show_contacts(contacts)
    elif choice == '3':
        delete_contact(contacts)
    elif choice == '4':
        select_contact(contacts)
    elif choice == '5':
        modify_contact(contacts)
    elif choice == '0':
        if confirm("是否保存通讯录？（y/n）"):
            save_contacts(contacts)
        break
    else:
        print("无效指令，请重新选择")