from django.urls import path
from .views import my_expense

urlpatterns = [
    path('cost_list/',my_expense)
    
]
