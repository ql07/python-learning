student = {"name": "路飞", "age": 19, "major": "CS"}

print(student["name"])
student["city"] = "东海岸"
student["age"] = 20

print(student.get("phone"))
print(student["phone"])

for k, v in student.items():
    print(k, "=", v)