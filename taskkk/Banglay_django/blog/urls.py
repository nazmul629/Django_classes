from django.urls import path
from .views import blog_list,detail_post

urlpatterns = [
    path('all_post/',blog_list),
    path('detile_post/<int:post_id>',detail_post,name="post_datiles")

]