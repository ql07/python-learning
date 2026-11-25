# 字典在内存，JSON在磁盘

字典是程序运行期间存在于内存里的一份临时数据，程序一关就蒸发；
JSON 是磁盘上的一个文本文件，不随程序关闭消失。
它们是同一份通讯录的两种形态——save() 写成 JSON，load() 还原成字典。

## 今天踩的坑

屏幕上出现的不等于我写过的：AI 补全把练习 2 的代码投到我眼前，
让我误以为 contacts.json 不存在。不是自己写的代码，要检查再信。

## 类比

账号密码备忘录：输入平台名称，返还密码。但光有字典不够——
程序关了密码表就蒸发，必须 save() 落盘成 JSON，下次 load() 取回。

## 示例

import json

def save(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)          # 用 return 交货，别用 loaded 憋在函数里

