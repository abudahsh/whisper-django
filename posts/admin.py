from django.contrib import admin

# Register your models here.
from posts.models import Comment, Whisper

admin.site.register(Whisper)
admin.site.register(Comment)