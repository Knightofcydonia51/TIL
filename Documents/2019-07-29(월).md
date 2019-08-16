# Web Service

> Web: 월드와이드웹(WWW). 인터넷에 연결된 컴퓨터들을 통해 사람들이 정보를 공유할 수 있는 정보 공간.
>
> 고객(사용자)의 요청에 대한 응답을 주는 것.(from server, computer)



## 요청의 종류

1. 줘라(Get) : url에 직접 요청을 입력하는 방식 (길이제한 존재)
2. 받아라(Post) : 숨겨져서(body안에) 보내진다. (form을 이용해 submit)



- IP (Internet Protocol) : 8비트의 숫자로 구성된 숫자의 집합으로, 각자가 가지고 있는 주소와 동일하다.

  ex) 172.217.27.78

  

- 도메인(Domain Name Service) : 네트워크상의 컴퓨터를 식별하는 호스트명(사람에게 읽기 쉽게 이름 부여)

  ex) google.com

  

- URL(Uniform Resource Locator) : 도메인 + 경로

  ex) https://www.google.co.kr/search?q=구글



### static web

> 정적 웹. 어떤 요청이 오든 정해진 하나의 응답밖에 못함. 접속 시마다 같은 응답을 함. 
>
> ex) 학교 홈페이지, 댓글 기능이 없는 블로그



### Dynamic web

> 동적 웹.  플라스크처럼 우리가 요청하는 것을 변환해서 응답해줌.
>
> ex) 댓글, 게시물 작성이 가능한 홈페이지



### HTML(Hyper Text Markup Language)

- 기존의 텍스트 : 페이지의 순서에 따라 글을 읽음. (선형적)

- 하이퍼 텍스트 : 순서와 상관없이 링크를 통해 문서를 넘나들며 읽어 나감. (비선형적)



### HTTP(Hyper Text Transfer Protocol)

> 하이퍼텍스트를 주고받는 통신규약



### CSS(Cascading Style Sheet)

> HTML 상태의 문서를 보기에 좋게, 이쁘게 가시화시켜줌.



- 요소 (Element)

HTML의 요소는 태그와 내용으로 구성되어 있다.

태그는 대소문자를 구별하지 않으나, 소문자로 작성해야 한다.

요소간 중첩도 가능하다.



- 속성(attribute)

태그에는 속성이 지정될 수 있다.



a 태그

```html
<a href="https://developer.mozilla.org/ko/" target="_blank">모질라 재단</a>

href="#" 을 할시 하이퍼링크는 활성화시키면서 실제로는 이동하지 않는다.
a 태그 안에 image 태그를 포함시켜 응용 가능.
target 속성에 blank를 추가하면 새 창에 띄울 수 있다.
```





미디어 태그

``` html
이미지
<img src="/profile.jpg"/>

추가 속성
tableindex :
alt : 이미지가 로드되지 않을 때 띄울 화면
width
height

<video src="/video.mp4"/>
<iframe src="https://www.w3schools.com"></iframe>
width
height
```



시맨틱 태그

컨텐츠의 의미를 설명하는 태그로서, HTML5에 새롭게 추가된 시맨틱 태그가 있다.

<div>이것은 공간</div> -> division -> 공간 분할



- element:nth-child() : 해당하는 태그의 순서 기준으로 해당
- element:nth-of-type() : 부모 속성 밑에서 특정 태그를 가진 자식 속성만 해당
- 둘이 겹칠시 nth of type이 우선시됨.



```html
<div>
   <p>test line 1</p>
   <span>test line 2</span>
   <p>test line 3</p>
   <p>test line 4</p>
   <span>test line 5</span>
</div>

<style>
   p:nth-of-type(2) { color: red; } # p태그 가진 것들중 2번째가 빨간색으로 변경 line3
   p:nth-child(2) { color: blue; } # line2가 변경 
   p:nth-child(4) { color: green; }
   span:nth-child(1) { color: orange; }
   span:nth-of-type(1) { color: yellow; }
</style>
```

