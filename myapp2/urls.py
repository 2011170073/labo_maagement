from django.urls import path
from . import views
from . import models

urlpatterns = [
    path("",views.teacher_list_view.as_view()),
    path("<int:pk>",views.status_list_view.as_view(),name="status_list_page"),
    path("update",views.status_update.as_view())
]