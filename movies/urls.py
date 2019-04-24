from django.urls import path

from movies.views import MovieListCreateAPIView

app_name = 'movies'
urlpatterns = [
    path(r'', MovieListCreateAPIView.as_view(), name='list_create_movies')
]