from django.db import models

# Create your models here.


class User(models.Model):
    First_name = models.TextField()
    Middle_name = models.TextField()
    Last_name = models.TextField()
    User_name = models.TextField(unique=True)
    password = models.TextField()
    phone_number = models.TextField()
    Middle_name = models.TextField()
    Gender = models.TextField()
    Date_of_birth = models.DateTimeField(null=True)