from django.db import models
from django.conf import settings


class Podcast(models.Model):
    url = models.URLField()
    description = models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)



class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    podcast = models.ForeignKey('podcasts.podcast', related_name='favourites', on_delete=models.CASCADE)