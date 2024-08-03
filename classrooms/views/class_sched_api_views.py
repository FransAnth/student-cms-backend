from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from classrooms.models import ClassSchedule
from classrooms.serializers import ClassScheduleSerializer


class ClassScheduleView(APIView):

    def get(self, request):
        class_sched_id = request.query_params.get("id")
        classroom_id = request.query_params.get("classroomId")
        class_sched_qs = ClassSchedule.objects.all()

        try:
            if class_sched_id != None:
                class_sched_qs = class_sched_qs.filter(id=class_sched_id)

            elif classroom_id != None:
                class_sched_qs = class_sched_qs.filter(classroom_id=classroom_id)

            serializer = ClassScheduleSerializer(class_sched_qs, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as error_message:
            return Response(
                data={"message": str(error_message)}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        class_schedule = {
            "date": request.data.get("date"),
            "start_time": request.data.get("startTime"),
            "end_time": request.data.get("endTime"),
            "classroom_id": request.data.get("classroomId"),
            "course_id": request.data.get("courseId"),
        }

        serializer = ClassScheduleSerializer(data=class_schedule)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            class_sched = ClassSchedule.objects.get(id=id)
        except ClassSchedule.DoesNotExist:
            return Response(
                {"message": "Class schedule does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        class_sched.delete()
        return Response(
            {"message": "Class Schedule successfully deleted"},
            status=status.HTTP_200_OK,
        )
