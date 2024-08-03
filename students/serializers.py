from rest_framework import serializers

from classrooms.models import Classroom
from classrooms.serializers import ClassroomDetailsSerializer
from courses.models import Course
from courses.serializers import CourseSerializer

from .models import Student, StudentSchedule


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "middle_initial", "last_name", "address"]


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentSchedSerializer(serializers.ModelSerializer):
    classroom = ClassroomDetailsSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    student = StudentDetailsSerializer(read_only=True)
    classroom_id = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), write_only=True, source="classroom"
    )
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), write_only=True, source="course"
    )
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), write_only=True, source="student"
    )

    class Meta:
        model = StudentSchedule
        fields = "__all__"
