from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from classrooms.models import Classroom
from classrooms.serializers import ClassroomDetailsSerializer, ClassroomListSerializer
from student_cms.utils.pagination import CustomPageNumberPagination


class ClassroomApiView(APIView):

    def get(self, request):
        try:
            classroom_id = request.query_params.get("id")
            if classroom_id:
                classroom_query_set = Classroom.objects.filter(id=classroom_id)
                serializer_class = ClassroomDetailsSerializer

            else:
                classroom_query_set = Classroom.objects.order_by("-created_at")
                serializer_class = ClassroomListSerializer

            paginator = CustomPageNumberPagination()
            result_page = paginator.paginate_queryset(classroom_query_set, request)
            serializer = serializer_class(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)

        except Exception as error_message:
            return Response(
                data={"message": str(error_message)}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        serializer = ClassroomDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            classroom = Classroom.objects.get(id=id)
        except Classroom.DoesNotExist:
            return Response(
                {"message": "Classroom does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        classroom.delete()
        return Response(
            {"message": "Classroom successfully deleted"}, status=status.HTTP_200_OK
        )
