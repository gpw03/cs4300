from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from .models import Seat

# Create your views here.
def MovieViewSet(request):
    movies = Movie.objects.all().order_by("title")
    return render(request, "bookings/movie_list.html", {"movies": movies})

def SeatViewSet(request):
    seats = Seat.objects.all().order_by("movie")
    return render(request, "bookings/seat_booking.html", {"seats": seats})

def BookingViewSet(request):
    return HttpResponse("Booking view")
