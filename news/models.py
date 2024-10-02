# models.py
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    link = models.URLField(unique=True)
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
