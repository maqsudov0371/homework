from . import views
from django.urls import path

urlpatterns = [
    path('', views.cars),
    path('-user', views.company, name='company'),
    path('appeals', views.coder, name='coder')
]