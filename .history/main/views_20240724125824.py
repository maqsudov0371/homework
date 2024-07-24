from django.shortcuts import render
from . import models

def watches(request):
    return render(request, 'watches.html', context)