from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("records/", views.records_list, name="records_list"),
]
