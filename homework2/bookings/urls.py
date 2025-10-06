from django.urls import path

from . import views

urlpatterns = [
    path("", views.SeatViewSet, name="seat_booking"),
    path("", views.MovieViewSet, name="movie_list"),
    path("", views.BookingViewSet, name="booking_history"),
]