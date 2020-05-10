from .models import Game, Player
from .serializers import GameSerializer, PlayerSerializer
from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class GameCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayerCreate(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer