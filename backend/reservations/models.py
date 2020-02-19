from django.db import models
from lots.models import Lot
from clients.models import Client
from django.contrib.auth import get_user_model

class Reservation(models.Model):
    lot_id = models.ForeignKey(Lot, on_delete=models.CASCADE)
    broker_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['lot_id'], condition=models.Q(active=True), name='unique_reserved_lot')
        ]