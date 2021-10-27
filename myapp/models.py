from django.db import models

# Create your models here.
class students(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    course=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    contact=models.BigIntegerField()
    