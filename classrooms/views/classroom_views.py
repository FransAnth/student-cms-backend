from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from classrooms.models import Classroom
from classrooms.serializers import ClassroomSerializer


class ClassroomApiView(APIView):

    def get(self, request):
        classroom_id = request.query_params.get("id")
        classroom_query_set = Classroom.objects.all()

        try:
            if classroom_id != None:
                classroom_query_set = classroom_query_set.filter(id=classroom_id)

            serializer = ClassroomSerializer(classroom_query_set, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as error_message:
            return Response(
                data={"message": str(error_message)}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        classroom = {
            "name": request.data.get("name"),
            "code": request.data.get("code"),
            "building_name": request.data.get("buildingName"),
        }

        serializer = ClassroomSerializer(data=classroom)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

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
