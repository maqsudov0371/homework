from django.db import models
from django.contrib.auth.models import  AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='avatar', null=True)
    bio = models.TextField(null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

        
class Watches(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    


class WatchImg(models.Model):
    img = models.ImageField(upload_to='watches-img/')
    watch = models.ForeignKey(Watches, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.watch.title


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    watch = models.ForeignKey(Watches, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self) -> str:
        return f"{self.author.username} to {self.watch.title}"


class Appeal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    appeal = models.TextField()

    def __str__(self) -> str:
        return self.full_name