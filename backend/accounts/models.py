from django.db import models
from sales.models import Sale

class Account(models.Model):
    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
    payment_type = models.BooleanField()
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)