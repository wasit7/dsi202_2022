from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    def __str__(self):
        return "%s"%(self.name)
