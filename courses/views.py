from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from student_cms.utils.pagination import CustomPageNumberPagination

from .models import Course
from .serializers import CourseDetailsSerializer, CourseListSerializer


class CourseApiView(APIView):

    def get(self, request):
        course_id = request.query_params.get("id")
        course_query_set = Course.objects.all()
        paginator = CustomPageNumberPagination()

        try:
            if course_id is not None:
                course_query_set = course_query_set.filter(id=course_id)
                result_page = paginator.paginate_queryset(course_query_set, request)
                serializer = CourseDetailsSerializer(result_page, many=True)

            else:
                result_page = paginator.paginate_queryset(course_query_set, request)
                serializer = CourseListSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)

        except Exception as error_message:
            return Response(
                data={"message", str(error_message)}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        course = {
            "name": request.data.get("name"),
            "code": request.data.get("code"),
            "description": request.data.get("description"),
        }

        serializer = CourseDetailsSerializer(data=course)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            course = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response(
                {"message": "Course does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )

        course.delete()
        return Response(
            {"message": "Course successfully deleted"}, status=status.HTTP_200_OK
        )
