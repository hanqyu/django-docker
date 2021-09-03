# django-docker
django를 Docker & Github Action으로 배포해봅시다.

# 환경
- docker 
- docker-compose
- nginx
- gunicorn
- postgres
- python3.8
- django(>=3.0)

# 처음 해야할 일
1. 이 프로젝트는 django_docker라는 이름으로 되어 있습니다. 원하는 이름으로 바꾸시려면 모든 파일의 'django_docker' 를 모두 바꿔주시고 최상단 django_docker 폴더명도 바꿔주세요.
2. .env.example 파일의 값을 복사해서 .env 파일을 만들어줍니다. 
```
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
DATABASE=postgres
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST_AUTH_METHOD=trust
DJANGO_SECRET_KEY={django secret key}
``` 

3. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)에서 키를 생성하여 .env 파일 마지막 `DJANGO_SECRET_KEY`에 넣어줍니다.
4. 아래 [도커 실행해보기](#도커 실행해보기)를 수행해봅니다.

# 도커 실행해보기
1. `docker-compose -f docker-compose.yml up --build`
2. 127.0.0.1:8000 접속
3. `docker-compose -f docker-compose.prod.yml down -v` 로 종료

### Pycharm에서 간편히 docker를 실행하고 싶다면 
아래 문서를 참고해주세요
- 참고) [Pycharm docker-compose 설정](https://www.jetbrains.com/help/pycharm/docker-compose.html#working)

# 배포
배포 전에 AWS EC2 서버와 RDS db가 필요합니다.

아래 노션을 따라 만들어보세요.
[https://hanqyu.notion.site/django_docker-EC2-RDS-669e385c10164f8c82dddcbc2e60cfd4](https://hanqyu.notion.site/django_docker-EC2-RDS-669e385c10164f8c82dddcbc2e60cfd4)

### .env.prod 만들기
이 프로젝트의 최상단에 다음 값을 가진 .env.prod 파일을 만듭니다.
```
POSTGRES_HOST={RDS db 주소}
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DEBUG=False
DJANGO_ALLOWED_HOSTS={EC2 서버 ip 주소},
DJANGO_SECRET_KEY={django secret key}
```

### Github Action 설정
1. Github Secrets에 필요한 값 설정
    - ENV_VARS: .env.prod 전체 복사
    - HOST: 배포할 EC2 서버 public ip 주소
    - KEY: 배포할 EC2 서버로 접근 가능한 ssh key 전문
2. Actions 탭에서 실행해보거나 master에 push 되었을때 자동으로 배포되는지 확인


### 알아두면 좋은 점
- 소스는 ec2 ubuntu 기준 /home/ubuntu/srv/로 배포됩니다
- 배포 스크립트는 config/scripts/deploy.sh에 있습니다 

# Reference
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/ \
https://github.com/appleboy/ssh-action \
https://github.com/marketplace/actions/rsync-deployments-action \
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04 \
https://docs.docker.com/compose/install/
