scores = [88, 92, 75, 60, 100, 45]

excellent = [s for s in scores if s >= 80]   # 优秀名单
print("大于等于80的：", excellent)
print("最高分：", max(scores))
print("最低分：", min(scores))
print("平均分: ", round(sum(scores) / len(scores), 1))   # round保留1位
passed = [s for s in scores if s >= 60]      # 及格名单
print("及格名单", passed)
