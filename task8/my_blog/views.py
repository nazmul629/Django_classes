from django.shortcuts import render
from .models import Blog_Post,Catagory


def blog_list(request,catagori_name):
    all_post=Blog_Post.objects.filter(catagory__name=catagori_name)
    contex={'post_lists':all_post}
    return render(request,'blog/post_list.html',contex)   



def blog_datiles(request,num):
    all_post=Blog_Post.objects.get(id=num)
    contex={'post':all_post}
    return render(request,'blog/details_post.html',contex) 


def catagori_name(request):
    all_post=Catagory.objects.all()
    contex={'post_lists':all_post}
    return render(request,'catagori/catagory.html',contex) 

    

def greetings(request):
    if request.method=="POST":
        user = request.POST["username"]
        password = request.POST["password"]
        context= {"name":user,
                   "pass":password, 
        }
        return render(request,'blog/greeting.html',context)
    return render(request,'blog/greeting.html')

