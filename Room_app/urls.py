from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.roomlist_view.as_view(),name="roomlist"),
    path("shiratuti",views.RoomSiratutiView.as_view(),name="shiratuti"),
    path("update",views.RoomupdateView.as_view()),
]