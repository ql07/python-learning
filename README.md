# python-learning

我的 Python 自学仓库。费曼学习法：每天写代码 + 写一篇用自己的话讲懂概念的笔记。

## 项目亮点

**d4_contacts.py —— 菜单式通讯录（第一个完整小产品）**

- 增 / 查 / 删 + while 菜单循环
- json 持久化：启动自动读取存档，退出时询问是否保存，关机不丢数据
- 防呆处理：无效指令提示、删除前探路人名、同名联系人覆盖确认（y/n，大小写兼容）、空通讯录提示

## 目录结构
- d2/ ：D2~D3 练习代码（字典/循环 + 函数/异常/json 读写）
- d4/ ：D4 通讯录项目（d4_contacts.py，运行时在根目录生成 contacts.json 存档）
- notes/：费曼笔记（d2-notes：字典在内存、JSON在磁盘；d3-notes：函数与 return 等）

## 学到的东西

- **D1**：变量、字符串、input/print、基本运算
- **D2**：字典、for/while 循环、列表操作
- **D3**：函数与参数、return、import、try/except、json 读写、文件持久化
- **D4**：项目实战——用函数拆分功能、菜单循环、字符串方法（lower()）、容错与用户确认流程

## 环境说明

- Python 3.x，PyCharm + 虚拟环境（.venv）
- 运行方式：`python d4/d4_contacts.py`

## 学习计划

- [x] D1：入门基础
- [x] D2：字典与循环
- [x] D3：函数、异常、json 持久化
- [x] D4：通讯录项目（第一个能存档的小产品）
- [ ] D5：？
