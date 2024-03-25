from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Modify the AbstractUser class with additional
       fields, including: can_view_paint, can_edit_inventory, have_access
    """
    can_view_paint = models.BooleanField(default = False)
    can_edit_inventory = models.BooleanField(default = False)
    have_access = models.BooleanField(default = False)