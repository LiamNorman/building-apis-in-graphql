from django.db import models

class Station(models.Model):
    description = models.TextField()
    url = models.URLField()
    name = models.TextField()
    followers = models.IntegerField(null=True)
    active = models.BooleanField(default=False)