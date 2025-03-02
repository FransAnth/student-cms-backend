from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from classrooms.models import ClassSchedule
from classrooms.serializers import ClassScheduleSerializer
from student_cms.utils.pagination import CustomPageNumberPagination


class ClassScheduleView(APIView):

    def get(self, request):
        try:
            class_sched_id = request.query_params.get("id")
            classroom_id = request.query_params.get("classroomId")

            if class_sched_id:
                class_sched_qs = ClassSchedule.objects.filter(id=class_sched_id)
            elif classroom_id:
                class_sched_qs = ClassSchedule.objects.filter(classroom_id=classroom_id)
            else:
                class_sched_qs = ClassSchedule.objects.order_by("-created_at")

            paginator = CustomPageNumberPagination()
            result_page = paginator.paginate_queryset(class_sched_qs, request)
            serializer = ClassScheduleSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)

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
