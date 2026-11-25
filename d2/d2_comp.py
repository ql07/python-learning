scores = [88, 92, 75, 60, 100, 45]

passed = [s for s in scores if s>= 80]
print(passed)

doubled = [s * 2 for s in scores]
print(doubled)

print([n.capitalize() for n in ["tom", "jerry"]])