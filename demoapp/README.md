# Deployment notes


## Application based on
https://www.sankalpjonna.com/learn-django/building-a-django-crud-application-in-minutes

## Python version
3.8.13

## Freeze Python libraries
pip freeze > requirements.txt



## Build container 
```
from /Users/felipe/Documents/django/demoapp
docker build . -t docker-rest-django-v0.1.0
```

## Run container
run docker container docker run -d -p 8000:8000 docker-rest-django-v0.1.0


## to use mysql container:
docker run -d -p 3306:3306 --name mysql-docker-container -e MYSQL_ROOT_PASSWORD=p4ssw0rd* -e MYSQL_DATABASE=product_app_db -e MYSQL_USER=product_app_user -e MYSQL_PASSWORD=p4ssw0rd* mysql/mysql-server:latest

## apply migrations
python manage.py migrate

## Check
http://127.0.0.1:8000/records/details/0/