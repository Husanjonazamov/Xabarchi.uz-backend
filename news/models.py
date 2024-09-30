from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    published_on = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title
