from django.db import models

from courses.models import Course

# Create your models here.


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default=None)
    code = models.CharField(max_length=45, default=None)
    building_name = models.CharField(max_length=200, default=None)
    status = models.CharField(max_length=45, default="Available")


class ClassSchedule(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
