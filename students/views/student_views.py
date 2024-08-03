from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from students.models import Student
from students.serializers import StudentDetailsSerializer, StudentSerializer


class StudentView(APIView):

    def get(self, request):
        student_id = request.query_params.get("studentId")
        student_qs = Student.objects.all()

        try:
            if student_id != None:
                student_qs = student_qs.filter(id=student_id)
                serializer = StudentDetailsSerializer(student_qs, many=True)

            else:
                serializer = StudentSerializer(student_qs, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as error_message:
            return Response(
                data={"message": str(error_message)}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        student_data = {
            "first_name": request.data.get("firstName"),
            "middle_initial": request.data.get("middleInitial"),
            "last_name": request.data.get("lastName"),
            "performance": request.data.get("performance"),
            "address": request.data.get("address"),
            "birthday": request.data.get("birthday"),
        }

        serializer = StudentDetailsSerializer(data=student_data)
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
