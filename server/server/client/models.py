from django.db import models

# Create your models here.

class user_detail(models.Model):
    M = 'm'
    F = 'f'
    userID = models.TextField()
    userName = models.TextField()
    email = models.TextField()
    gender = ((M, 'male'), (F,'female'))
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)