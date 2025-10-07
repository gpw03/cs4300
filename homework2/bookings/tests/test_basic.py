import pytest
from django.urls import reverse
from datetime import date
from bookings.models import Movie

@pytest.mark.django_db
def test_movie_str():
    """Unit test: Checks that the Movie model's __str__ returns the title."""
    movie = Movie.objects.create(
        title="Inception",
        description="Dreams within dreams",
        release_date=date(2010, 7, 16),
        duration=148
    )
    # __str__ should return the title
    assert str(movie) == "Inception"


@pytest.mark.django_db
def test_movie_list_view_returns_200(client):
    """Integration-lite test: Ensures the movie list page loads successfully."""
    # Create a sample movie
    Movie.objects.create(title="Dune", release_date=date(2021, 10, 22), duration=155)
    
    # Reverse looks up the URL by name (from urls.py)
    url = reverse("movie_list")
    response = client.get(url)

    # Check: the page loaded correctly (HTTP 200)
    assert response.status_code == 200

    # Check: the correct template was used
    assert any(t.name == "bookings/movie_list.html" for t in response.templates)


@pytest.mark.django_db
def test_api_movies_list(api_client):
    """Simple API test: GET /api/movies/ returns 200 and includes our movie."""
    Movie.objects.create(title="Matrix", release_date=date(1999, 3, 31), duration=136)
    response = api_client.get("/api/movies/")

    # The API should return HTTP 200
    assert response.status_code == 200

    # Check that the movie we created is in the JSON response
    titles = [m["title"] for m in response.json()]
    assert "Matrix" in titles
