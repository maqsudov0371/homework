from django.shortcuts import render
from . import models

def watches(request):
    context = {
        'post':posts,
        'img':img
    }
    
    return render(request, 'watches.html', context)