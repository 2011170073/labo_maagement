from django.urls import path
from . import views
from . import models

urlpatterns = [
    path("",views.teacher_list_view.as_view()),
    path("<int:pk>/list",views.status_list_view.as_view(),name="status_list_page"),
    path("<int:pk>/last",views.status_last_view.as_view()),
    path("update",views.status_update.as_view())
]