from rest_framework import serializers

from classrooms.models import Classroom
from classrooms.serializers import ClassroomDetailsSerializer
from courses.models import Course
from courses.serializers import CourseDetailsSerializer
from student_cms.utils.camel_case_serializer import CamelCaseSerializer

from .models import Student, StudentSchedule


class StudentListSerializer(CamelCaseSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "middle_initial", "last_name", "address"]


class StudentDetailsSerializer(CamelCaseSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentSchedSerializer(CamelCaseSerializer):
    classroom = ClassroomDetailsSerializer(read_only=True)
    course = CourseDetailsSerializer(read_only=True)
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
