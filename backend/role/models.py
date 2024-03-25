from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model that includes the various permissions and roles
    """
    can_view_paint = models.BooleanField(default = True)
    can_edit_paint = models.BooleanField(default = False)
    can_access = models.BooleanField(default = False)

