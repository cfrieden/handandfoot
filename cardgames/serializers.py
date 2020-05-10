from rest_framework import serializers
from .models import Game, Player

class PlayerOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name')

class GameOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'type')

class PlayerSerializer(serializers.ModelSerializer):
    games = GameOnlySerializer(many=True, read_only=True)
    
    class Meta:
        model = Player
        fields = ('id', 'name', 'games')

class GameSerializer(serializers.ModelSerializer):
    players = PlayerOnlySerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'type', 'players')

