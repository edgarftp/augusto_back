from django.db import models

class Subdivision(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    num_lots = models.IntegerField(default=0)
    private = models.BooleanField(default=False)
    club_house = models.BooleanField(default=False)
    amenites = models.BooleanField(default=False)
    park = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

