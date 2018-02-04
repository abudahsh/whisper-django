from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    pass


class WhisperBase(models.Model):
    creator=models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(model_name)s')
    text=models.TextField(max_length=200)
    image=models.ImageField(blank=True, null=True)
    likes=models.PositiveSmallIntegerField(default=0)
    categories=models.ManyToManyField(Category, null=True)
    comments=models.PositiveSmallIntegerField(default=0)
    time_stamp=models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract=True


class Whisper(WhisperBase):
    class Meta:
        abstract=False
        get_latest_by='time_stamp'


class Comment(WhisperBase):
    comment_on=models.ForeignKey(Whisper, on_delete=models.CASCADE)
    class Meta:
        abstract=False
        ordering=['-time_stamp']