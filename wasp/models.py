from django.db import models
class todo(models.Model):
  taskname=models.CharField(max_length=100)
  taskdate=models.DateField()
# Create your models here.
