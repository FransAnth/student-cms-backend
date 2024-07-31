from django.urls import path

from .views.class_sched_api_views import ClassScheduleView
from .views.classroom_api_views import ClassroomApiView

urlpatterns = [
    path("", ClassroomApiView.as_view()),
    path("<int:id>/", ClassroomApiView.as_view()),
    path("schedule/", ClassScheduleView.as_view()),
    path("schedule/<int:id>/", ClassScheduleView.as_view()),
]
