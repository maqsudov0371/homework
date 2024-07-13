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

        user = models.User.objects.create(
            username = name,
            email = email
        )
        user.set_password(password)
        user.save()

    return render(request, 'register.html') 