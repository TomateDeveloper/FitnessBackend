from django.db import models

from categories.models import Category


class Video(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    tag = models.ForeignKey(Category, on_delete=models.CASCADE)
