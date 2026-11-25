scores = [88, 92, 75, 60, 100, 45]

print(scores[0],scores[-1])
print(len(scores))
print(scores[1:3])
print(scores[:3])
print(scores[-2:])

scores.append(77)
scores[0] = 90
print(scores)
print(100 in scores)