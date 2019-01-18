from django.db import models
from django.urls import reverse

class Articles(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles')