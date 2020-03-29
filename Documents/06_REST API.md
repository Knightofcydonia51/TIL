## REST API



Restful의 가장 중요한 두가지 원칙은 다음과 같다. 



**첫 번째,** URI는 정보의 자원을 표현해야 한다. 

**두 번째,** 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다. 

예를 들면 사용자 정보를 삭제하는 메소드에 대해서 `GET /members/delete/1` 으로 표현하는 것이 아니라, `    DELETE /members/1`로 표현하는 것이다. 정보의 자원인 members를 URI에서 표현하고 있고, 그 행위에 대한 정의는 메소드를 통해 하고 있다.





## 참고

 https://meetup.toast.com/posts/92