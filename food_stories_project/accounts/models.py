from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField('Bio', null=True, blank=True)
    image = models.ImageField('Image', upload_to='user_images/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
