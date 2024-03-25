from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    can_view_paint = models.BooleanField(default = True)
    can_edit_paint = models.BooleanField(default = False)
    can_access = models.BooleanField(default = False)

