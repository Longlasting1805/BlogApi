from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000, default='')
    author = models.TextField()
    comment = models.TextField(max_length=1000, unique=True)
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class Comment(models.Model):
