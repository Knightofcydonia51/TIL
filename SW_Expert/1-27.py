students=[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
scores=0

while students:
    score=students.pop()
    if score>=80:
        scores+=score
print(scores)