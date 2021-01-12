from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    writer = models.CharField(max_length=64)
    description = models.TextField(default=' ')

    def __str__(self):
        return self.title
