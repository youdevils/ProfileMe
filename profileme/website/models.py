import enum
from django.db import models


# Create your models here.
class Person(models.Model):
    age = models.IntegerField(default=18)
    health = models.CharField(max_length=30)
    employed = models.BooleanField(default=False)
    businessOwner = models.BooleanField(default=False)
    married = models.BooleanField(default=False)
    homeOwner = models.BooleanField(default=False)
    renting = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    haveChildren = models.BooleanField(default=False)

          