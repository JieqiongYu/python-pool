from django.views.generic import (
    ListView, DetailView,
)

from django.shortcuts import render

# Create your views here.
from core.models import Movie
from core.models import Person

class MovieDetail(DetailView):
    queryset = Movie.objects.all_with_related_persons()

class MovieList(ListView): 
    model = Movie

class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()