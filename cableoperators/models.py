from django.db import models

class SitiNetwork(models.Model):
    sitiid = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    gender = models.BooleanField(default=True)
    phone=models.BigIntegerField(null=True)
    percentage=models.IntegerField(null=True)
    dob=models.DateField(max_length=15,null=True)


# Create your models here.
