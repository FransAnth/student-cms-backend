from django.db import models


# Create your models here.
class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default=None)
    code = models.CharField(max_length=45, default=None)
    building_name = models.CharField(max_length=200, default=None)
    status = models.CharField(max_length=45, default="Available")
