from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from accounts.models import Profile


class Category(models.Model):
    pass


class WhisperBase(models.Model):
    creator=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= '%(model_name)s')
    text=models.TextField(max_length=100)
    image=models.ImageField(blank=True, null=True, upload_to='whisper_images/', default='whisper_images/None/no-img.png')
    likes=models.PositiveSmallIntegerField(default=0)
    categories=models.ManyToManyField(Category, null=True, blank=True)
    comments=models.PositiveSmallIntegerField(default=0)
    time_stamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.creator.nickname +'  - '+ str(self.text[:18])

    class Meta:
        abstract=True


class Whisper(WhisperBase):
    def get_absolute_url(self):
        return reverse('posts:whisper-detail', args=[str(self.id)])
    class Meta:
        abstract=False
        get_latest_by='-time_stamp'


class Comment(WhisperBase):
    comment_on=models.ForeignKey(Whisper, on_delete=models.CASCADE)
    class Meta:
        abstract=False
        ordering=['-time_stamp']