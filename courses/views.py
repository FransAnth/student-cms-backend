from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializers import CourseSerializer


class CourseApiView(APIView):

    def get(self, request):
        course_id = request.query_params.get("id")
        course_query_set = Course.objects.all()

        try:
            if course_id != None:
                course_query_set = course_query_set.filter(id=course_id)

            serializer = CourseSerializer(course_query_set, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

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

        serializer = CourseSerializer(data=course)

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
