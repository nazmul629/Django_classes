from django.urls import path
from .views import *

urlpatterns = [
     path('category/',category_name),
     path('post_list/<int:id>',post_list,name="post_list_urls"),
     path('detail_post/<int:num>',post_details,name = 'datiles_post_url'),
     path('login/',user_login),
     path('add_book/',add_book),
     path("book_list/",all_book,name= 'book_list'),
     path('add_book/',add_book),
     path('delete_book/<int:id>',delete_book, name ="delete-book"),
     path('edit_book/<int:id>',edit_book, name="edit-book"),

     path ('add_account/',add_account, name = "add-account"),
     path('acc_list/',all_account),
     path('check_blance/',check_balance, name = "check_blance_urls")
]