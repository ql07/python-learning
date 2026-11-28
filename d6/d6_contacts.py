from contacts_store import load_contacts, save_contacts
from contacts_ops import add_contact, show_contacts, delete_contact, query_contact, modify_contact, confirm

def main():
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
            query_contact(contacts)
        elif choice == '5':
            modify_contact(contacts)
        elif choice == '0':
            if confirm("是否保存通讯录？（y/n）"):
                save_contacts(contacts)
            break
        else:
            print("无效指令，请重新选择")

if __name__ == "__main__":
    main()