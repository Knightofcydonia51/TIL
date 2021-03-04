# Routrip 프로젝트

## 프로젝트 개요

- 여행 계획을 짜는데 있어서 시간 절약이 목표
- 직접 그곳을 다녀온 다른 사람들의 경험을 통해 공유
- Restful API 에 기반해 작성됨.(Restful에 대한 내용은 여기를 참조: https://meetup.toast.com/posts/92[^각주1] )
- http://52.78.8.59:8083/ (현재는 배포 중단)



## 다른 서비스와의 차별점

- 루트를 가시화해 직관성을 높임.
- 여행 기간(ex:1박 2일, 2박 3일, 당일)을 필터링할 수 있어 큐레이션 기능을 강화.



## 사용한 언어들, API

- 프로그래밍 언어: Javascript, Node.js, Java
- 프레임워크: SpringBoot, MyBatis, Vue, Vuetify
- DB: mariaDB
- 사용 라이브러리: 인증-JWT, 암호화-BCrypt, 테스트-Swagger, Postman
  모달 폼 - Sweertalert2
  데이터 요청 - Axios, jquery
  외부 연동 API: 로그인-카카오, ImageUpload-Imgur 




## 개발 측면에서의 알게된 점

- vue.js, javascript의 문법
- jwt 토큰의 사용 방법
- Axios 비동기 요청으로 백엔드와 통신하는 방법
- Backend 개발자가 구체적으로 하는 일
- Frontend 개발자가 구체적으로 하는 일
- Jira를 안정적으로 사용할 수 있는 것의 장점



### Spring backend와 vue.js 기반 frontend 간의 통신 방법

- 기본적으로 backend에서 요청값과 반환값을 코드로 짜놓는다.

- 원리는 형식에 알맞은 요청이 들어오면,  요청에 해당하는 쿼리문을 실행해 DB와 통신을 하고, DB로부터 요청에 맞는 값을 불러와 응답을 하게 된다.

- Routrip 프로젝트에서는 Swagger를 통해 백엔드 개발자가 이를 정해 두었고, 프론트엔드는 Swagger를 통해 원활한 소통을 하며 개발할 수 있었다.

- 특이사항으로 delete 요청을 할 때는 비동기 요청시 data로 한번 더 요청값을 감싸 주어야 했다.

```javascript
 Axios.delete('http://192.168.100.70:8083/account/user/',
                        {   data:{
                            jwt: jwt,
                            password: value}
                        }
                    ).then(res => {}
```

  

### jwt 토큰(Json Web Token)

- 토큰 기반 인증 방식으로, 사용자의 세션 상태를 저장하는게 아니라 토큰 body로 저장해 사용자가 가지고 있고 그것을 증명서처럼 사용하는 방식이다.
- Routrip 프로젝트에서는 토큰을 필요로 하는(로그인 했을때만 보여줘야하는) 페이지마다 올바른 토큰을 담아 요청을 했을 시에만 응답을 하도록 설계하였다.
- localStorage에서 토큰을 받아오는 함수인 getInfo 함수와 받은 토큰으로 사용자 정보(id, email 등)를 요청하는 reqInfo 함수를 mounted 해놓고 사용하였다.



### async & await 요청

- 백엔드나 웹과 통신할 때 요청의 순서를 정하기 위해 콜백 함수 대신 사용하는 방법
- 한마디로 비동기 요청인데, 사용자 데이터를 받아온 후 이를 바탕으로 다른 요청을 보내야 하는 상황이라면 사용자 데이터를 받아오는 함수가 선행되고 이후 작업이 시행되어야 한다.
- Sweetalert을 사용할 때와 jwt를 받아온 후 jwt를 바탕으로 사용자 정보를 받아올 때 주로 사용하였다.



### imgur API

- imgur.com에서 제공하는 API로, id값과 secret값을 발급받아 알맞은 요청을 보낼 시 이미지를 업로드해주고, url를 제공해준다.
- 이 API를 사용하는 것으로 사용자 프로필 사진, 글 사진 등과 같은 자료들을 local에 저장하지 않고 웹에 할당할 수 있게 되었고, 많은 자원을 절약할 수 있었다.



```javascript
사용 예시(참고 : https://hsol.tistory.com/938 )


test(){
            var file = document.getElementById('file');
            var image = document.getElementById('image');
            console.log(file)
            console.log(image)
            file.onchange = function (event) {
                var target = event.currentTarget;
                var xmlHttpRequest = new XMLHttpRequest();
                xmlHttpRequest.open('POST', 'https://api.imgur.com/3/image/', true);
                xmlHttpRequest.setRequestHeader("Authorization", "Client-ID ddbe62505149f6d");
                xmlHttpRequest.onreadystatechange = function () {
                if (xmlHttpRequest.readyState == 4) {
                    if (xmlHttpRequest.status == 200) {
                    var result = JSON.parse(xmlHttpRequest.responseText);
                    image.src = result.data.link;
                    var look = result.data.link;
                    console.log(result);
                    console.log(look)
                    }
                    else {
                        alert("업로드 실패");
                    image.src = "http://dy.gnch.or.kr/img/no-image.jpg";
                    }
                }
            };
            xmlHttpRequest.send(target.files[0]);
            image.src = "https://nrm.dfg.ca.gov/images/image-loader.gif";
            };

```



### 개발 외

- 매일 할일을 정해놓고 하면 생산성이 엄청나게 늘어난다.
- 매일 아침 간단한 회의를 하는게 중요하다.(데일리 스크럼 미팅)
- 그 날 있었던 이슈들을 간략하게 정리해놓고, 차후에 문서화하면 오래 기억할 수 있다.



[^각주1]:  Restful의 가장 중요한 두가지 원칙은 다음과 같다. **첫 번째,** URI는 정보의 자원을 표현해야 한다. **두 번째,** 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다. 예를 들면 사용자 정보를 삭제하는 메소드에 대해서 `GET /members/delete/1` 으로 표현하는 것이 아니라, `    DELETE /members/1`로 표현하는 것이다. 정보의 자원인 members를 URI에서 표현하고 있고, 그 행위에 대한 정의는 메소드를 통해 하고 있다.

