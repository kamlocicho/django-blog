from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70, blank=False)
    content = models.CharField(max_length=500, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"{self.author.username} - {self.title}"