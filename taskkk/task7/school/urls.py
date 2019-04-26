from django.urls import path
from .views import all_students,st_result,district

urlpatterns = [
    path('all_student/',all_students, name= "students"),
    path('result/',st_result,name= "result"),
    path('district/',district,name= "district"),
    # path('roll/',all_roll,name= "separateet_roll"),
 
 


]