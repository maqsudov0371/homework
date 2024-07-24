from django.shortcuts import render
from . import models

def watches(request):

    return render(request, 'watches.html', context={'list': 'Mashinalar ro`yxati'})


def register_user(request):
    return render(request, 'register.html', context={'list1': 'Ko ro`yxati'}) 


def appeals(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        appeal = request.POST['appeals']

        appeals = models.Appeal.objects.create(
            username = name,
            email = email,
            appeal = appeal
        )
        appeals.save()
    return render(request, 'appeals.html')