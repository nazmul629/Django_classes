from django.shortcuts import render
from .models import Expense
 
 
def my_expense(request):
    expenses = Expense.objects.all()
    context = {'expenses': expenses}
    return render(request, 'cost/expense.html', context)