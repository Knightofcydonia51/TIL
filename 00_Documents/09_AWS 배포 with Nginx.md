## .pem 파일이 있을 때 aws에 배포하는 방법 with nginx

- putty 설치
- https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/putty.html

- 위 링크를 따라서 하되, 도메인 주소 입력은 해당 인스턴스의 환경에 맞게 입력(ex: ubuntu@**public DNS**)
- 서버에 접속이 완료되면, 필요한 코드를 내려받는다. 보통 git에 올라가 있으니 git clone을 하면 됨.



## nginx 설정

- 설치

```
$ sudo apt-get install nginx

$ nginx -v
nginx version: nginx/1.4.6 (Ubuntu)
```



- aws 서버에 프로젝트 clone

```
/usr/share/nginx/html/
$ git clone {git https}
```



- node.js, npm install

```
$ sudo apt-get update 
$ sudo apt-get install nodejs
$ sudo apt-get install npm

node -v
npm -v
```



- 프로젝트 내, package.json 이 있는 경로에서 npm install

```
/{project_dir}
npm install

# node_modules 생성된거 확인하기

npm build
```



- 할당된 주소로 들어가보기(ex: http://k02d1101.p.ssafy.io/)
- 디폴트 index.html인 welcome to nginx 페이지 확인
- 디폴트 conf 파일의 루트 디렉토리를 배포할 프로젝트 빌드 산출물 경로로 변경할 것.







sudo systemctl restart nginx





netstat -ano

pid확인



포트가 nginx에서 이미 사용중일때

curl localhost로 작업 확인

ps -ef | grep nginx

pid 확인

마스터(root) 작업 kill

이후 다시 restart하면 작동



 /usr/share/nginx/html;

/home/ubuntu/s02p31d110/frontend/dist

/usr/share/nginx/html/s02p31d110/frontend/frontEnd/dist



nginx 안될때 해결법 