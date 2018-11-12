from django.db import models

# Create your models here.
def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()
