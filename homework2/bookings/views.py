from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import transaction 
from .models import Movie, Seat, Booking
from rest_framework import viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all().order_by("title")
    return render(request, "bookings/movie_list.html", {"movies": movies})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        user_name = request.POST.get("user").strip()
        seat = get_object_or_404(Seat, pk=seat_id, movie=movie)

        if seat.status == Seat.Status.BOOKED:
            messages.warning(request, f"Seat {seat.seat_number} is already booked.")
            return redirect("seat_booking", movie_id=movie.id)

        seat.status = Seat.Status.BOOKED
        seat.save()
        Booking.objects.create(movie=movie, seat=seat, user=user_name)
        messages.success(request, f"Booked seat {seat.seat_number} for {movie.title}.")
        return redirect("booking_history")


    seats = movie.seats.all().order_by("seat_number")
    return render(request, "bookings/seat_booking.html", {"movie": movie, "seats": seats})

def booking_history(request):
    bookings = (
        Booking.objects.select_related("movie", "seat")
        .order_by("-booking_date")
    )
    return render(request, "bookings/booking_history.html", {"bookings": bookings})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by("title")
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.select_related("movie").all().order_by("seat_number")
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related("movie", "seat").all().order_by("-booking_date")
    serializer_class = BookingSerializer