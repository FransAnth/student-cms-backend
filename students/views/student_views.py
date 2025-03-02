from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from student_cms.utils.pagination import CustomPageNumberPagination
from students.models import Student
from students.serializers import StudentDetailsSerializer, StudentListSerializer


class StudentView(APIView):

    def get(self, request):
        try:
            student_id = request.query_params.get("id")
            if student_id:
                student_qs = Student.objects.filter(id=student_id)
                serializer_class = StudentDetailsSerializer

            else:
                student_qs = Student.objects.order_by("-enrollment_date")
                serializer_class = StudentListSerializer

            paginator = CustomPageNumberPagination()
            result_page = paginator.paginate_queryset(student_qs, request)
            serializer = serializer_class(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)

        except Exception as error_message:
            return Response(
                data={"message": str(error_message)}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        serializer = StudentDetailsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requet, id):
        try:
            student = Student.objects.get(id=id)

        except Student.DoesNotExist:
            return Response(
                {"message": "Student does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        student.delete()
        return Response(
            {"message": "Student successfully deleted"}, status=status.HTTP_200_OK
        )
