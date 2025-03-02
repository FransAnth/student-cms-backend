from django.urls import path

from .views.class_sched_views import ClassScheduleView
from .views.classroom_views import ClassroomApiView

urlpatterns = [
    path("", ClassroomApiView.as_view()),
    path("schedule/", ClassScheduleView.as_view()),
]
