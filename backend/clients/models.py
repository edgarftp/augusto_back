from django.db import models
from django.contrib.auth import get_user_model

class Client(models.Model):
    name = models.CharField(max_length=250, blank=False)
    email = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    brokerID = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        unique_together = ('name', 'email',)