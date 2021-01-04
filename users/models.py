from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.db import models


class Userc(AbstractUser):
    """model for users"""

    profile_img = models.ImageField(upload_to='pm', null=True)
    bio = RichTextUploadingField(null=True, blank=True)
    followers = models.ManyToManyField('Userc', blank=True)
