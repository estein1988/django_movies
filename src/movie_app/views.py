from django.shortcuts import render
from rest_framework import viewsets

from .models import Actor, Director, Movie
from .serializers import ActorSerializer, DirectorSerializer, MovieSerializer

# Create your views here.

class ActorView(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class DirectorView(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



#simliart to rails contoroller