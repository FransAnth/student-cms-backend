from django.db import models
from django.utils import timezone

from courses.models import Course

# Create your models here.


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default=None, unique=True)
    code = models.CharField(max_length=45, default=None, unique=True)
    building_name = models.CharField(max_length=200, default=None)
    status = models.CharField(max_length=45, default="Available")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["created_at"]
        db_table = "classrooms"


class ClassSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["created_at"]
        db_table = "classroom_scheds"
