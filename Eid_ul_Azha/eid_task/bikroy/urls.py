from django.urls import path
from .views import *

urlpatterns = [
    path('home/',city_name),
    path('item_list/category/<category_name>',post_list,name="post_list_urls"),
    path('item_list/location/<location_name>',product_list,name="product_list_location"),
    path('item_deails/<int:num>',post_details,name="details_urls"),

    path('login/',user_login),
    path('add-account/',add_account, name= "add_account_urls"),
    path('all_account/',all_account, name = "all_account_url"),
    path('cheke_blance/',cheke_blance, name = "chekke-blance-urls" )
    
]