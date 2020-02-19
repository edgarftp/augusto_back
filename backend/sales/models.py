from django.db import models
from django.utils import timezone
from lots.models import Lot
from clients.models import Client
from django.contrib.auth import get_user_model

class Sale(models.Model):
    lot_id = models.ForeignKey(Lot, on_delete=models.DO_NOTHING)
    broker_id = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    sales_price = models.FloatField()
    approval = models.BooleanField(default=True)
    total_comission = models.FloatField()
    broker_comission = models.FloatField()
    sale_date = models.DateField(default=timezone.now)
    active = models.BooleanField(default=True)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['lot_id'], condition=models.Q(active=True), name='unique_sold_lot')
        ]

