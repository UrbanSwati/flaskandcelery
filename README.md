# Flask App with Celery

To start up rabbitmq in docker
```docker
docker run -p 15672:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3.6-management-alpine
```