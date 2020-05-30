from django.db import models

from categories.models import Category


class Video(models.Model):
    tag = models.ForeignKey(Category, on_delete=models.CASCADE)
