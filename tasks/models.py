from django.db import models

# Create your models here.
class Post1(models.Model):
    STUFF = [
        ('Oxygen','Oxygen'),
        ('Plasma','Plasma'),
    ]
    #quantity = 
    needs = models.CharField(max_length=50, choices=STUFF)
    nameofp = models.CharField(max_length=50)
    ageofp = models.IntegerField()
    state = models.CharField(max_length=20)
    address1 = models.CharField(max_length=25)
    address2 = models.CharField(max_length=25)
    pincode = models.IntegerField()
    contact1 =  models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering = ('-created_on',)

class Post2(models.Model):
    STUFF = [
        ('Oxygen','Oxygen'),
        ('Plasma','Plasma'),
    ]
    #quantity = 
    supply = models.CharField(max_length=50, choices=STUFF)
    nameofp = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    address1 = models.CharField(max_length=25)
    address2 = models.CharField(max_length=25)
    pincode = models.IntegerField()
    contact1 =  models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering = ('-created_on',)

