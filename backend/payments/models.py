from django.db import models
from accounts.models import Account

class Payment(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)