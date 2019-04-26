from django.urls import path
from .views import all_info,detail_post

urlpatterns = [
    path('all_profile',all_info,name="all_list"),
    path('profile/<int:post_id>',detail_post,name="posts")
    
 
]
