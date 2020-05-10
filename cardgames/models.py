from django.db import models

# Create your models here.
class Game(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        ordering = ['type']
    
    def __str__(self):
        return self.type

class Player(models.Model):
    name = models.CharField(max_length=100)
    games = models.ManyToManyField(Game, related_name="players")

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name