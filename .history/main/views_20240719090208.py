from django.shortcuts import render
from . import models

def watches(request):

    return render(request, 'watches.html', context={'list': 'Mashinalar ro`yxati'})


def register_user(request):
    return render(request, 'register.html', context={'list1': 'Kompaniyalar ro`yxati'}) 


def appeals(request):
    return render(request, 'appeals.html', context={'list': ' ro`yxati'})