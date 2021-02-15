from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    designer = models.CharField(max_length=50)
    year_released = models.CharField(max_length=10)
    number_of_players = models.IntegerField()
    estimated_time = models.CharField(max_length=20)
    age_recommendation = models.IntegerField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)