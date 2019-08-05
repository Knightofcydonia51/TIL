list=[88,30,61,55,95]
for i, k in enumerate(list):
    if int(k) >= 60:
	    print("{}번 학생은 {}점으로 합격입니다.".format(i+1, k))
    else:
        print("{}번 학생은 {}점으로 불합격입니다.".format(i+1,k))