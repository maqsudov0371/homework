from django.shortcuts import render
from . import models

def cars(request):

    return render(request, 'watches.html', context={'list': 'Mashinalar ro`yxati'})


def cars(request):
    return render(request, 'register.html', context={'list1': 'Kompaniyalar ro`yxati'}) 


def coder(request):
    return render(request, 'appeals.html', context={'list2': 'Dasturlash tillari ro`yxati'})