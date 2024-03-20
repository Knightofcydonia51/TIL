# Docker 명령어

```bash
# centOs7 이미지 pull
docker pull centos:{want_version}
ex) docker pull centos:7

# 이미지 조회
docker images

# 컨테이너 조회
docker ps -a

# 컨테이너 실행
docker start <CONTAINER_NAME>

# 파일 전송
전송할 파일  컨테이너명:저장할 파일 경로
docker cp alldb.dmp oracle10g:/alldb.dmp

# 실행중인 컨테이너에 명령어 실행
docker exec <CONTAINER_ID> <COMMAND>

# 실행중인 컨테이너에 접속
docker exec -it <CONTAINER_ID> /bin/bash

# 컨테이너를 Commit하여 image 만들기
docker commit {commit할 컨테이너명} {만들어질 image 명}

# docker image push
계정과 연결하려면,
이미지 이름에
Docker Hub 계정 이름(Docker Hub의 네임스페이스)을 포함해야 합니당

그렇지 않았을 경우 docker login 해도 레포로 푸시가 되지 않습니다.

해결방법은

이미지명 앞에 Docker Hub 계정을 붙여서
(Docker Hub 계정)/docker-repo:first-image 와 같이 새로 만들어줍니다.

tag를 변경해줍니다.
$ docker tag first-image (Docker Hub 계정)/docker-repo:first-image
$ docker push (Docker Hub 계정)/docker-repo:first-image

# docker image build
docker build -t <원하는 Docker 이미지 이름>:<tag명> .

# docker container 만들고 실행하기
$ docker run -it -d <이미지 명>:<tag 명>

# docker container 만들고 실행하기 -p 옵션(포트)
$ docker run -it -d -p <외부port>:<컨테이너 내부 port> --name <원하는 컨테이너 이름> <이미지 명>:<tag명>
ex) $  docker run -it -d -p 8080:80 --name <원하는 컨테이너 이름> <이미지 명>:<tag명>

# 열린 포트 확인
docker port <컨테이너명>

# 서비스자동실행 참고
https://compeople.tistory.com/175
```



- ssh 접속 설정하기
- https://it-sunny-333.tistory.com/66



- centos 환경에서 실행한 컨테이너 systemctl 명령어 안 먹힐때

```bash
[user01@master ~]$ docker run -it centos:7 bash
[root@9fa1db10b89c /]# systemctl
Failed to get D-Bus connection: Operation not permitted

# hostOS Terminal
$ docker run --privileged -d --name mycentos centos:7 /sbin/init
$ docker exec -it mycentos /bin/bash
```





### VM 사용하다가 docker 사용하면 오류뜨는 현상 해결

- windows 기능 켜기/ 끄기에서 hyper-v 체크하기
- cmd창 관리자 권한으로 실행한 후 bcdedit /set hypervisorlaunchtype auto 입력



# Dockfile 문법

- 빌드는 docker desktop이 실행되어 있는 상태에서 진행한다.
- dockerfile은 확장자가 따로 없으며, dockerfile이 위치한 디렉토리 내에서 docker build -t [태그명] . 명령어로 빌드한다.

```
FROM [이미지명]
생성할 이미지의 베이스가 될 이미지를 명시 Docker hub에 등록된 image 중에 선택할 수 있다.
ex) FROM openjdk:8-jdk-alpine

RUN [실행할 명령어]
이미지를 만들기 위해 컨테이너 내부에서 명령어를 실행
RUN 명령어에 ["/bin/bash", "echo hello" >> test.html"] 같이 입력하면 /bin/bash 셸을 이용해 'echo hello >> test2.html'을 실행한다는 뜻

VOLUME [호스트의 디렉토리]
VOLUME 명령어를 통해 호스트 디렉토리를 docker container 내부와 연결 시킬 수 있습니다. 데이터소스, 로그파일, 설정파일등을 docker container 외부로 노출 시키고자 할 때 사용할 수 있다.

ADD [파일명]
호스트 컴퓨터의 파일을 컨테이너 내부의 특정 디렉토리로 복사하는 역할을 합니다.COPY 명령어와 유사하나 ADD는 http:// URL에 등록된 파일도 복사 할 수 있는 기능이 있습니다.
* ADD, COPY 모두 복사할 소스 파일은 docker build를 실행시키는 디렉토리에 위치하고 있어야 합니다.

COPY [파일명]
호스트 컴퓨터의 파일을 컨테이너 내부의 특정 디렉토리로 복사하는 역할을 합니다.ADD 명령어와 달리 URL에 등록된 파일은 복사가 안됩니다.

ENV [환경변수명] [환경변수 값]
ex) JAVA_HOME="/var/openjdk"

ENTRYPOINT [실행할 커맨드][커맨드 인자값]
FROM으로 생성된 이미지 내에서 실행할 명령어를 입력한다
스크립트 형식으로 사용할 수 있다
ex) "java", "-jar", "/app.jar"


FROM openjdk:8-jdk-alpine   
RUN apk add --no-cache curl tar bash
VOLUME /tmp
ADD build/libs/gs-rest-service-0.1.0.jar app.jar
ENV JAVA_OPTS=""
ENTRYPOINT ["java","-jar","/app.jar"]
```

