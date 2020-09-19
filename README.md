# django-docker
장고를 도커 + circleci로 배포해봅시다

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

# Reference
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/