from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)


class Post(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=100)
    body = models.TextField()
