from django.shortcuts import render
from . import models

def watches(request):
    posts = models.Watches.objects.all()
    img = models.WatchImg.objects.all()
    context = {
        'post':posts,
        'img':img
    }
    
    return render(request, 'watches.html', context)
