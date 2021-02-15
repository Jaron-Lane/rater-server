from django.db import models

class Review(models.Model):
    review = models.CharField(max_length=200)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)