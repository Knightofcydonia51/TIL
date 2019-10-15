from django.shortcuts import render
from faker import Faker
from .models import Job
from decouple import config
import requests
from pprint import pprint

def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    name=request.POST.get('name')
    person=Job.objects.filter(name=name).first() #filter=값이 없을 때도 오류를 내지 않게 해줌

    # DB에 이름이 있을 경우
    if person:
        past_job=person.past_job
    # DB에 이름이 없을 경우
    else:
        fake=Faker()
        past_job=fake.job()
        person=Job(name=name, past_job=past_job)
        person.save()

    # GIPHY 
    #1. API key 가져오기
    GIPHY_API_KEY=config('GIPHY_API_KEY')
    #2. 요청 URL 세팅
    url=f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1'
    #3. 실제 요청을 보내자. (json -> dict)
    data=requests.get(url).json()
    #4. image 추출
    try:
        image=data.get('data')[0].get('images').get('original').get('url')
    except IndexError:
        image=None
    # NAVER IMAGE
    #1. 요청 헤더 정보 준비
    NAVER_ID= config('NAVER_ID')
    NAVER_SECRET=config('NAVER_SECRET')
    headers={
        'X-Naver-Client-Id': NAVER_ID,
        'X-Naver-Client-Secret':NAVER_SECRET 
        }
    #2. 요청 URL 준비
    naver_url=f'https://openapi.naver.com/v1/search/image?query={past_job}&filter=medium&display=1'
    

    #3. 실제 요청 보내기
    naver_data=requests.get(naver_url, headers=headers).json()
    pprint(naver_data)
    
    
    #4. 이미지 링크 추출하기
    naver_image=naver_data.get('items')[0].get('link')
    context={'person':person, 'image':image, 'naver_image':naver_image}
    
    return render(request, 'jobs/past_life.html',context)

'''
V5WpcdtgesmrzYOycXqzLDbY9UOaJlrT
[urls]
- url 분리
- app_name,path name 설정

[views]
- index : index.html 랜더링
- past_life : 사용자가 form으로 넘긴 데이터와 faker
라이브러리를 활용해 전생 직업 생성
1. 사용자가 form을 통해 날린 이름을 받는다.
2. DB에 사용자에게 받은 이름이 존재하는지 확인
- 존재하면 : 기존 사용자의 past_job을 past_job이라는 변수에 저장
- 존재 x : faker를 활용하여 새로운 직업을 생성하고 입력받은 사용자 이름과 생성한 직업을 DB에 저장
3.context로 담아서 past_life.html로 넘김

[templates]
- 템플릿 구조는 app/templates/app
- base.html : 기존 프로젝트 폴더에서 확장
- index.html : 사용자에게 자신의 이름을 입력할 수 있는 form 제공
- past_life.html : context로 넘겨 받은 데이터를 출력
ex) {{person.name}}님의 전생 직업은 {{person.past_job}}입니다.


'''