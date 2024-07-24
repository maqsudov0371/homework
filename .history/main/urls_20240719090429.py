from . import views
from django.urls import path

urlpatterns = [
    path('', views.cars),
    path('company', views.company, name='company'),
    path('coder', views.coder, name='coder')
]