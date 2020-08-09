
def solution(files):
    answer = []

    info=[]
    for i in range(len(files)):
        head = ""
        number=""
        tail=""
        hnt=[]
        cnt=0
        flag=[0,0]
        for k in files[i]:
            if flag[0]==0:
                if k.isdigit()==0:
                    head+=k
                else:
                    flag[0]=1
                    number+=k
                    hnt.append(head)
            else:
                if flag[1]==0:
                    if k.isdigit()==1 and cnt<5:
                        number+=k
                        cnt+=1
                    else:
                        flag[1]=1
                        tail+=k
                        hnt.append(number)
                        number = ""
                else: # tail
                    tail+=k
        if number:
            hnt.append(number)
        hnt.append(tail)
        hnt.append(i)
        info.append(hnt)

    info= sorted(info, key=lambda x: (x[0].lower(), int(x[1])) )

    for i in range(len(info)):
        text=""
        for k in range(3):
            text+=info[i][k]
        answer.append(text)
    return answer

files=["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files= ["h1111","F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat","h11111"]
print(solution(files))