from django.db import models

from students.models import Student


# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default=None)
    code = models.CharField(max_length=45, default=None)
    description = models.CharField(max_length=500, default="")
    status = models.CharField(max_length=20, default="Available")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
