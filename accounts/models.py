from django.contrib.auth.models import User
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
    owner=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nickname=models.CharField(max_length=80, default=generate_nickname)
    age=models.IntegerField(choices=Ages)
    rating=models.FloatField(default=5.0)
    number_of_ratings=models.PositiveSmallIntegerField(default=0)
    location=models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.nickname