from django.urls import path
from . import views
from . import models

urlpatterns = [
    path("",views.teacher_list_view.as_view()),
    path("<int:pk>",views.status_list_view.as_view()),
    path("update",views.status_update.as_view())
]