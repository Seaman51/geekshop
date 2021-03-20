from datetime import timedelta
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    activation_key = models.CharField(max_length=64, blank=True, null=True)
    activation_key_expires = models.DateTimeField(default=now() + timedelta(hours=48))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True
