from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content=models.TextField(max_length=9999,null=True)
