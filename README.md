# SupportService
The project is intended for the support service. 


#docker-compose
docker-compose up --build

docker exec -it support_service_web bash
python manage.py collectstatic
python manage.py createsuperuser

#redis start
docker run -d -p 6379:6379 redis
#workerstart
celery -A config  worker -l info

