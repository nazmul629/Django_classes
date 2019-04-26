from django.contrib import admin
from .models import Catagory,BlogPost,Book,BankAccount

admin.site.register(BankAccount)
admin.site.register(Catagory)
admin.site.register(BlogPost)
admin.site.register(Book)
