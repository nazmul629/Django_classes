from django import forms
from.models import BankAccount



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class AddBookFrom(forms.Form):
    name = forms.CharField()
    price = forms.IntegerField()

class AccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = '__all__'

class ChakBalanceForm(forms.Form):
    account_no = forms.CharField()