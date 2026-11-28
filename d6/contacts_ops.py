
def confirm(prompt):
    while True:
        sure = input(prompt)
        if sure.lower() == 'y':
            return True
        elif sure.lower() == 'n':
            return False
        else:
            print("请重新输入！")


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

def delete_contact(contacts):
    deletes = input("请输入要删人的姓名：")
    if deletes in contacts:
        del contacts[deletes]
    else:
        print("未找到联系人姓名")


def query_contact(contacts):
    querys = input("请输入查询人姓名：")
    found = False
    for k, v in contacts.items():
        if querys in k:
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

def show_contacts(contacts):
    if not contacts:
        print("通讯录是空的")
    else:
        for k, v in contacts.items():
            print(k, "-", v)