from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Creating routing
router = DefaultRouter()
router.register(r"movies", views.MovieViewSet)
router.register(r"seats", views.SeatViewSet)
router.register(r"bookings", views.BookingViewSet)

urlpatterns = [
    path("movies/", views.movie_list, name="movie_list"),
    path("movies/<int:movie_id>/seats/", views.seat_booking, name="seat_booking"),
    path("bookings/", views.booking_history, name="booking_history"),
    # API section
    path("api/", include(router.urls)),
]