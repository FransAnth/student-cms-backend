from django.urls import path

from .views import ClassroomApiView

urlpatterns = [
    path("", ClassroomApiView.as_view()),
    path("<int:id>/", ClassroomApiView.as_view()),
]
