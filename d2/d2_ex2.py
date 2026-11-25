import json

contacts = {
    "路飞": "13800000001",
    "索隆": "13800000002",
    "娜美": "13800000003",
}

name = input("要查谁的电话：")
phone = contacts.get(name)
if phone is None:
    print("通讯录没有这个人")
else:
    print(name, "的电话是", phone)

with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts, f, ensure_ascii=False, indent=2)
with open("contacts.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)


for name, phone in loaded.items():
    print(f"{name}: {phone}")