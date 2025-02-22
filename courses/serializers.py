from rest_framework import serializers

from student_cms.utils.camel_case_serializer import CamelCaseSerializer

from .models import Course


class CourseListSerializer(CamelCaseSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "code", "status"]


class CourseDetailsSerializer(CamelCaseSerializer):
    class Meta:
        model = Course
        fields = "__all__"
