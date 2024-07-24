from . import views
from django.urls import path

urlpatterns = [
    path('', views.cars),
    path('register-user', views.register_user, name='register_user'),
    path('appeals', views.appeals, name='appeals')
]