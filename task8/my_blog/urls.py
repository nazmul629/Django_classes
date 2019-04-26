from django.urls import path
from .views import blog_list,blog_datiles,catagori_name,greetings

urlpatterns = [
    path('category/<catagori_name>',blog_list,name='item_list'),
    path('details/<int:num>',blog_datiles,name='datiles_post'),
    path('category/',catagori_name),
    path('greetings/',greetings)

] 