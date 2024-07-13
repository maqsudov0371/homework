from . import views
from django.urls import path

urlpatterns = [
    path('', views.watches),
    path('register-user', views.register_user, name='register_user'),
    path('appeal', views.appeal, name='appeal')
]