from django.db import models

# Create your models here.

class Users(models.Model):
    userid = models.CharField(max_length=4, primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)