from django.contrib.auth.models import Users
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

def create_user_profile( sender, instance,created ,**kwargs):
    