from django.urls import path

from .views.student_sched_views import StudentSchedView
from .views.student_views import StudentView

urlpatterns = [
    path("", StudentView.as_view()),
    path("<int:id>/", StudentView.as_view()),
    path("schedule/", StudentSchedView.as_view()),
    path("schedule/<int:id>/", StudentSchedView.as_view()),
]
