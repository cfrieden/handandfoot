from .models import Game
from .serializers import GameSerializer
from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class GameCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
