from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=80, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
