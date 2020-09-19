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


# Docker
## development
1. `docker-compose -f docker-compose.yml up --build`
2. 127.0.0.1:8000 접속
3. `docker-compose -f docker-compose.prod.yml down -v` 로 종료

- 참고) [Pycharm docker-compose 설정](https://www.jetbrains.com/help/pycharm/docker-compose.html#working)

## production
1. `docker-compose -f docker-compose.prod.yml up --build`
2. 127.0.0.1 접속
3. `docker-compose -f docker-compose.prod.yml down -v` 로 종료

# Deploy
1. Github Action 설정 확인 (.github/workflows/deploy.yml)
2. Github Secrets에 필요한 값 설정
    - ENV_FILE: .env file에 들어갈 key-value 값 전체
    - HOST: 배포할 remote 서버 host
    - USERNAME: 배포할 remote 서버의 username _ex) ubuntu_
    - KEY: 배포할 remote 서버로 접근 가능한 ssh key 전문

- 소스는 ec2 ubuntu 기준 /home/{username}/srv/django-docker로 배포됩니다

# Reference
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
https://github.com/appleboy/ssh-action
https://github.com/marketplace/actions/rsync-deployments-action