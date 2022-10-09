from turtle import title
from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
