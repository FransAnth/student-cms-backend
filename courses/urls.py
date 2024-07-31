from django.urls import path

from .views import CourseApiView

urlpatterns = [
    path("", CourseApiView.as_view()),
    path("<int:id>/", CourseApiView.as_view()),
]
