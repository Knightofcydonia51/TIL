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
