from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    saved_posts = models.ManyToManyField('Post', blank=True)

    def __str__(self) -> str:
        return self.first_name
    

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True)
