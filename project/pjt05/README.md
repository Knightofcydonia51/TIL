# 05 - Django 프레임워크를 활용한 영화 DB



## 01. 사용한 API

- 해당사항 없음.



## 02. HTML 파일 목록

### - index.html

- 영화 목록을 표시하는 메인 페이지입니다.
- 각 필드는 title(String), title_en(String), audience(Integer), open_date(Date), genre(String), watch_grade(String), score(Float), poster_url(Text), description(Text) 로 구성되어 있습니다.



### - new.html

- 영화 데이터를 생성하는 양식을 포함하고 있는 HTML입니다.
- views.py/create 함수로 컬럼 데이터를 전송하는 역할입니다.



### - edit.html

- 작성된 영화 정보를 수정하는 역할을 하는 HTML입니다.
- 수정이 완료되면 update.html을 띄우게 됩니다.



### - update.html

- 영화 정보 수정이 완료되었음을 알리는 HTML 파일입니다.



### - update.html

- 영화 정보 수정이 완료되었음을 알리는 HTML 파일입니다.



### - detail.html

- 영화의 모든 컬럼을 포함하고 있는 상세 정보를  표시하는 HTML입니다.
- 정보 수정, 삭제 등의 기능을 하는 HTML로 이동할 수 있습니다.



### - update.html

- 영화 정보 수정이 완료되었음을 알리는 HTML 파일입니다.



## 03. 상세정보

- 9개 컬럼으로 구성된 영화 정보를 입력하고, 저장하며 이를 관리할 수 있는 서비스입니다.
- Django 프레임워크 환경에서 작성되었으며, DB와 python, html간 기초적인 데이터 교환을 확인할 수 있습니다.