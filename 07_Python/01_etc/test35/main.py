


hansot={'메가스팸마요':5600, '스팸마요':3600}
print('사람 수?')
n=int(input())
print('배달비?')
delivery_fee=int(input())
answer=[]
for i in range(n):
    a_option=''
    a_fee = 0

    print('사람, 메뉴?')
    a, a_food=map(str,input().split())
    print('곱빼기나 라면?')
    a_option=input()
    a_fee=hansot.get(a_food)
    if a_option:
        if a_option == '곱':
           a_fee+=+300

        elif a_option=='곱라면':
            a_fee+=+ 1100
    a_fee+=delivery_fee//n
    answer.append([a,a_fee])

for i in answer:
    for k in i:
        print(k, end=" ")
    print()


