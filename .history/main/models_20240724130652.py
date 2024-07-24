from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    saved_posts = models.ManyToManyField('Post', blank=True)

    def __str__(self) -> str:
        return self.first_name
    
class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_summa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    total_qty = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self) -> str:
        return self.user.username
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    color = models.CharField(max_length=100)
    count = models.DecimalField(max_digits=5, decimal_places=2, null=True )
    category_id = models.ForeignKey


class Cart_product(models.Model)
    ...