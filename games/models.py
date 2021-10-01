from django.db import models

# Create your models here.
class games(models.Model):
    game_title = models.CharField(max_length=255)
    year = models.IntegerField()
    dowload_links = models.CharField(max_length=300)
    
    def __str__(self):
        return self.game_title
