from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from student_cms.utils.pagination import CustomPageNumberPagination
from students.models import StudentSchedule
from students.serializers import StudentSchedSerializer


class StudentSchedView(APIView):

    def get(self, request):
        """
        Getting the schedule of a specific student
        """
        try:
            student_id = request.query_params.get("id")
            student_sched_qs = StudentSchedule.objects.order_by("-created_at")

            if student_id:
                student_sched_qs = student_sched_qs.filter(student_id=student_id)

            paginator = CustomPageNumberPagination()
            result_page = paginator.paginate_queryset(student_sched_qs, request)
            serializer = StudentSchedSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)

        except Exception as error_message:
            return Response(
                {"message": str(error_message)}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        serializer = StudentSchedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            student_schedule = StudentSchedule.objects.get(id=id)

        except StudentSchedule.DoesNotExist:
            return Response(
                {"message": "Schedule does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        student_schedule.delete()
        return Response(
            {"message": "Schedule successfully deleted"}, status=status.HTTP_200_OK
        )
