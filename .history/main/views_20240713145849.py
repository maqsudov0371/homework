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
        name = request.POST['name'],
        email = request.POST['email'],
        password = request.POST['password']

        models.User.objects.create(
            usernamename = name,
            email = email,
            password = password 
        )
    return render(request, 'register.html') 