<h1>SupportService</h1>
<p>The project is intended for the support service.</p>

Technology stack:
    <li>Django</li>
    <li>DRF</li>
    <li>Celery+Redis</li>
 
 [https://t.me/AlexStash](https://t.me/AlexStash) Автор
    
  Installation
  ------------
<p>Docker-compose</p>

    docker-compose up --build
    docker exec -it support_service_web bash
    python manage.py collectstatic
    python manage.py createsuperuser

<p>Redis start</p>

    docker run -d -p 6379:6379 redis

<p>Worker start</p>
    
    celery -A config  worker -l info

