# week02 data modeling

Design: https://docs.google.com/presentation/d/1moI1dgqOI9kojIAUoiUduJK7A1yuDUoWnCJ9mfTHQdI/edit#slide=id.g10f0a06f902_0_5 

Instruction: https://docs.google.com/document/d/1Rhr9L8du3RaN2tlS_1xvEt8HFKSpTula6ou1pb4TAX0/edit 

# Instruction

1. Create folder week02
    ````mkdir week02````
    ````cd week02/````
    ````conda activate dsi202_2022````
2. Start a new Project 
    ````django-admin startproject myproject````
3. Start a new app
    ````cd myproject````
    ````python manage.py startapp myapp````
4. Edit /myapp/models.py
````
from django.db import models

class Car(models.Model):
    maker = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
````
5. Edit /myapp/admin.py
````
from django.contrib import admin
from myapp.models import Car

class CarAdmin(admin.ModelAdmin):
    list_display=['model','maker']
    
admin.site.register(Car,CarAdmin)
````
6. Edit settings.py
````
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
````
7. Create schema and database
    ````python manage.py makemigrations````
    ````python manage.py migrate````
    ````python manage.py createsuperuser````
8. Go to the admin page and edit the car record
    1. ````python manage.py runserver 0.0.0.0:8002````
    2. go to http://localhost:8002/admin
    3. Edit data
    4. And capture the image
