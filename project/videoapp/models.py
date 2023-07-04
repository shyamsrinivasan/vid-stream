from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Videos(models.Model):
    """model class to store info on a given video"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_name = models.CharField(max_length=100)
    upload_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

    pass
