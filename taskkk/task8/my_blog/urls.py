from django.urls import path
from .views import blog_list,blog_datiles,catagori_name,greetings,search_post,search_categori,search_both

urlpatterns = [
    path('category/<catagori_name>',blog_list,name='item_list'),
    path('details/<int:num>',blog_datiles,name='datiles_post'),
    path('category/',catagori_name),
    path('greetings/',greetings),
    path('search_from/',search_post),
    path('search_result/',search_post),
    path('search_categori/', search_categori),
    path('categori_result/',search_categori),
    path('search_both/', search_both),
    path('both_result/',search_both)
    

] 