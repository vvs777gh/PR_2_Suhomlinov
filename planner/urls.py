from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("trips/<int:trip_id>/delete/", views.delete_trip, name="delete_trip"),
    path("trips/clear/", views.clear_trips, name="clear_trips"),
]
