student1 = 90, 80
student2 = 85, 75
student3 = 90, 100

for idx, student in enumerate([student1,student2,student3]):
    print('{}번 학생의 총점은 {}점이고, 평균은 {}입니다.'.format(idx+1, sum(student), sum(student)/len(student)))