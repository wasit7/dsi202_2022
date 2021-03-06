from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=5)
    mobile = models.CharField(max_length=20,blank=True)
    email = models.EmailField()

    def __str__(self):
        return "%s"%(self.email)

class Item(models.Model):
    UNIT_NAME_CHOICE = [
        ("ลูก","ลูก"),
        ("กก.","กิโลกรัม"),
        ("ชิ้น","ชิ้น")
    ]
    title = models.CharField(max_length=100)
    unit = models.CharField(
        max_length=5,
        choices=UNIT_NAME_CHOICE,
        default="ชิ้น",
    )
    unit_price = models.DecimalField(max_digits=5, decimal_places=2) #999.99
    image=models.ImageField(upload_to='myimages') #from week05
    description=models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return "%s"%(self.title)

class Order_Item(models.Model):
    profile = models.ForeignKey( Profile, on_delete=models.CASCADE)
    item = models.ForeignKey( Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return "profile:%s, item:%s, quantity:%s, unit: %s, unit_price:%s"%(self.profile.name,self.item, self.quantity, self.item.unit, self.item.unit_price)