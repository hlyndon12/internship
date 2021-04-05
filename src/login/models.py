from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    number = models.IntegerField(null=True)
    User = models.OneToOneField(User,on_delete=models.CASCADE,null = True)
    
    
