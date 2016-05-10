# Django_Celery_Ejemplo
Ejemplo de configuracion de Django y Celery.

#Ejecutar Django
```python manage.py runserver 8080```

#Ejecutar Celery
```python manage.py celery worker -A django_celery_tutorial.celery --loglevel=info```
