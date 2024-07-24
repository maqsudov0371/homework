from . import views
from django.urls import path

urlpatterns = [
    path('', views.cars),
    path('register-user', views.company, name='register_user'),
    path('appeals', views.coder, name='coder')
]