from django.urls import path

from . import views

app_name = "songs"
urlpatterns = [
    path("get_name", views.get_name, name="get_name"),
    path("song", views.song, name="song"),
]
