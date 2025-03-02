from django.db import models
from django.utils import timezone

from classrooms.models import Classroom
from courses.models import Course


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=90, default=None)
    middle_initial = models.CharField(max_length=5, default=None)
    last_name = models.CharField(max_length=90, default=None)
    performance = models.CharField(max_length=45, default="Not set")
    address = models.CharField(max_length=200, default=None)
    birthday = models.DateField(default=None)
    updated_at = models.DateTimeField(default=timezone.now)
    enrollment_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["enrollment_date"]
        db_table = "students"


class StudentSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["created_at"]
        db_table = "student_scheds"
