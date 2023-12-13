from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    name = models.TextField(max_length=64)
    short = models.TextField(max_length=64)
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name="courses")

class Item(models.Model):
    description = models.TextField(max_length=64)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="items")
    due = models.DateTimeField()
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name="items")
