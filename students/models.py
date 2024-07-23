from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=90, default=None)
    middle_initial = models.CharField(max_length=5, default=None)
    last_name = models.CharField(max_length=90, default=None)
    grade = models.IntegerField(default=None)
    address = models.CharField(max_length=200, default=None)
    birthday = models.DateField(default=None)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
