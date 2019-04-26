from django.shortcuts import render
from .models import Blog_post

# Create your views here.
def blog_list(request):
    post_list=Blog_post.objects.all()
    contex={'post_lists':post_list}
    return render(request,'blog/post_list.html',contex)

def detail_post(request,post_id):
    try:
        post=Blog_post.objects.get(id = post_id)
        contex={'details_post':post}
        return render(request,'blog/details_post.html',contex)
    except Exception as error:
            print(error)
            return render(request,'blog/404.html')


