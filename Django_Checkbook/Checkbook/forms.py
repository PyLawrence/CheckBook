from django import forms
from .models import Account, Transaction

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
