from django.shortcuts import render
from . import models

def watches(request):
    posts = models.Watches.objects.all()
    for post in posts:
        post.img = models.WatchImg.objects.filter(watch__id=post.id).last().img

    context = {
        'post':posts
    }
    return render(request, 'watches.html', context)


def register_user(request):
    if request.method == 'POST':
        print(request.POST['name'])
        print(request.POST['password'])

        models.User.objects.c
    return render(request, 'register.html') 