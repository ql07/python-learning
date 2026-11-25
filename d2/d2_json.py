import json

notes = {"d1": "搭环境+博客", "d2": "列表字典与JSON"}

with open("notes.json", "w", encoding="utf-8") as f:
    json.dump(notes, f, ensure_ascii=False, indent=2)

with open("notes.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["d2"])