from rest_framework import serializers

from courses.models import Course
from courses.serializers import CourseSerializer

from .models import Classroom, ClassSchedule


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"


class ClassScheduleSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    classroom_id = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), write_only=True, source="classroom"
    )
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), write_only=True, source="course"
    )

    class Meta:
        model = ClassSchedule
        fields = "__all__"
