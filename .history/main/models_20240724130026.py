from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    saved_posts = models.ManyToManyField('Post', blank=True)

    def __str__(self) -> str:
        return self.first_name
    
class Card(models)