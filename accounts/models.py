from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .names import generate_nickname
from django.db import models

# Create your models here.

class Profile(models.Model):
    Ages=(
        (1, '14-16'),
        (2, '17-19'),
        (3, '20-24'),
        (4, '25-30'),
        (5, '31-40'),
        (6, '+40')
    )
    owner=models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    nickname=models.CharField(max_length=80, default=generate_nickname) #found in accounts.names.py
    age=models.IntegerField(choices=Ages, null=True, blank=True)
    rating=models.FloatField(default=5.0)
    number_of_ratings=models.PositiveSmallIntegerField(default=0)
    location=models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.nickname



#signals that auto-create profile when a user object is created

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()