from datetime import datetime

from django.db import models


TRANSACTION_TYPES = [
    ('withdrawal', 'withdrawal'),
    ('deposit', 'deposit'),
]

# Create your models here.
class Account(models.Model):
    # ended up defining defaults for everything due to migration issues, leaving them as-is
    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    initial_deposit = models.DecimalField(max_digits=300, default='0.00', decimal_places=2)

    Accounts = models.Manager()

    def __str__(self):
        # cast firstname to string so pycharm will quit complaining
        return str(self.firstName) + ' ' + self.lastName

class Transaction(models.Model):
    date = models.DateField(default='')
    type = models.CharField(max_length=50, choices=TRANSACTION_TYPES, default=TRANSACTION_TYPES[0])
    amount = models.DecimalField(max_digits=100, default='0.00', decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default='')
    description = models.TextField(max_length=300, default='', blank=True)

    Transactions = models.Manager()