from django.db import models

class Car(models.Model):
    maker = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.DecimalField( max_digits=12, decimal_places=2, null=True)
    color = models.CharField(max_length=10,null=True)
    date = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return "%s %s %s"%(self.pk, self.maker, self.model)


class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=5)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    def __str__(self):
        return "%s %s"%(self.pk, self.email)

class Rent(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, null=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)
    rent_date = models.DateField(auto_now_add=True) #on create
    return_date = models.DateField(null=True, blank=True) #on update
    cost = models.DecimalField( max_digits=6, decimal_places=2, null=True, blank=True)
