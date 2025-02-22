from rest_framework import serializers

from courses.models import Course
from courses.serializers import CourseDetailsSerializer
from student_cms.utils.camel_case_serializer import CamelCaseSerializer

from .models import Classroom, ClassSchedule


class ClassroomListSerializer(CamelCaseSerializer):
    class Meta:
        model = Classroom
        fields = ["id", "name", "building_name", "status"]


class ClassroomDetailsSerializer(CamelCaseSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"


class ClassScheduleSerializer(CamelCaseSerializer):
    classroom = ClassroomDetailsSerializer(read_only=True)
    course = CourseDetailsSerializer(read_only=True)
    classroom_id = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), write_only=True, source="classroom"
    )
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), write_only=True, source="course"
    )

    class Meta:
        model = ClassSchedule
        fields = "__all__"
