from django.shortcuts import render
from .models import Profile


def all_info(request):
    post_list=Profile.objects.all()
    contex={'post_list':post_list}
    return render(request,'info/info_post.html',contex)


def detail_post(request,post_id):
    try:
        post=Profile.objects.get(id = post_id)
        contex={'details_post':post}
        return render(request,'info/info_details.html',contex)
    except Exception as error:
            print(error)
            return render(request,'blog/404.html')