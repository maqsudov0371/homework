from django.shortcuts import render
from . import models

def watches(request):
    posts = models.Watches.objects.all()

    context = {
        'post':posts
    }
    for post in context['post']:
        print(dir(post)
    return render(request, 'watches.html', context)


def register_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        user = models.User.objects.create(
            username = name,
            email = email
        )
        user.set_password(password)
        user.save()

    return render(request, 'register.html') 


def appeals(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        appeal = request.POST['appeals']

        appeals = models.Appeal.objects.create(
            username = name,
            email = email,
            appeal = appeal
        )
        appeals.set__ap(appeal)
        appeals.save()
    return render(request, 'appeals.html')