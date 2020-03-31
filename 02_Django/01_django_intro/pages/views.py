from django.shortcuts import render
from datetime import datetime
import random
import requests

# 기본 변수
def index(request):
    return render(request, 'pages/index.html') #리턴값 render의 인자는 반드시 request와 html이 포함되야 한다.

def introduce(request):
    return render(request, 'pages/introduce.html')

#2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context={'pick': pick}
    return render(request, 'pages/dinner.html', context) #3번째 인자는 반드시 딕셔너리

def lorempic(request):
    return render(request, 'pages/lorempic.html')

#3. variable Routing(동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context={
        'name': name,
        'age': age, 
        'pick': pick
        }
    return render(request, 'pages/hello.html', context)

#4. 실습
#4-1. 동적 라우팅을 활용해서(name과 age를 인자로 받아) 자기소개 페이지 만들기
def introduce2(request, name, age):
    context={
        'name': name,
        'age': age
        }
    return render(request, 'pages/introduce2.html', context)

#4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셉 결과를 출력
def mul(request, num1, num2):
    num3=num1*num2
    context={
        'num1': num1,
        'num2': num2,
        'num3': num3
    }
    return render(request, 'pages/mul.html', context)

#4-3. 반지름을 인자로 받아 원의 넓이를 구하시오.
def circle(request, r):
    ans=3.14*(r**2)
    context={
        'r':r,
        'ans':ans
    }
    return render(request, 'pages/circle.html',context)

#5. DTL(Django Template Language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Too fast to live, Too young to die'
    messages=['apple', 'banana', 'cucumber', 'mango']
    datetimenow=datetime.now()
    empty_list=[]

    context={
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow
    }
    return render(request, 'pages/template_language.html', context)

#6. 실습
#6-1. isbirth

def isbirth(request, my_birth):
    today=datetime.now()
    validate=False
    if str(today.month)+str(today.day)==my_birth:
        validate=True
    context={
        'my_birth': my_birth,
        'validate': validate,
    }
    return render(request, 'pages/isbirth.html', context)

#6-2. 회문판별(palindrome)
#회문이면(반대로 돌려도 같은 글자 -ex. racecar) '회문입니다.'
#아니면 '회문이 아닙니다.'
def ispal(request, pal):
    validate=False
    if pal==pal[::-1]:
        validate=True
    context={
        'pal':pal,
        'validate':validate,
    }
    return render(request, 'pages/ispal.html', context)

#6-3. 로또 번호 추첨
# lottos -> 1~45까지의 번호 중 6개를 랜덤으로 pick한 리스트
# real_lottos -> [21,24,30,32,40,42]
#1. lottos 번호를 하나씩 출력
#2. 컴시기가 뽑은 로또 번화와 실제 로또 번호 비교

def lotto(request):
    real_lottos = [21,24,30,32,40,42]
    lottos= list(random.sample(range(1,46),6))
    context={
        'real_lottos': real_lottos,
        'lottos': lottos,
    }

    return render(request, 'pages/lotto.html', context)

#7. Form - GET
def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message=request.GET.get('message')
    message2=request.GET.get('message2')
    context={
        'message': message, 
        'message2': message2,
    }
    return render(request, 'pages/catch.html', context)

def ping(request):
    return render(request, 'pages/ping.html')
   
def pong(request):
    message=request.GET.get('message')
    context={
        'message': message,
    }
    return render(request, 'pages/pong.html', context)

#8. Form - GET 실습(아스키 아티)
def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다.(GET)
    word=request.GET.get('word')

    #2. ARTII api로 요청을 보내 응답 결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 fonts(list)로 바꾼다.
    fonts=fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서
    #font라는 변수에 저장
    font=random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 font를 가지고 다시
    # 요청을 보낸다. 그리고 응답 결과를 result에 저장한다.
    result=requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context={
        'result': result,
    }
    return render(request, 'pages/result.html', context)

#9.Form - POST
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    context={
        'name':name,
        'password':pwd,
    }
    return render(request, 'pages/user_create.html', context)

#10. 정적 파일
def static_example(request):
    return render(request, 'pages/static_example.html')