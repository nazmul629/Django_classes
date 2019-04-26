from django import forms
from .models import BankAccount

class userlogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField()



class AccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = '__all__'


class ChekeBalanceForm(forms.Form):
    account_no = forms.CharField()