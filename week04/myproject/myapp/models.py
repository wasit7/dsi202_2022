from django.db import models

class Student(models.Models):
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50)
    email = models.Email()
    phone_number = models.CharField(max_length=11)
