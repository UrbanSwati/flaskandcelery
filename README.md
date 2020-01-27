# Flask App with Celery

To start up rabbitmq in docker, you first need to pull the image, then run the image with the following environment varibles 
```docker
docker pull rabbitmq:3.6-management-alpine
```

To start the image
```docker
docker run -p 15672:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3.6-management-alpine
```
