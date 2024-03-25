from django.db import models

# Create your models here.

class Paint(models.Model):
    PAINT_CHOICES = (
        ('red', 'Red'),
        ('grey', 'Grey'),
        ('black', 'Black'),
        ('white', 'White'),
        ('purple', 'Purple'),
    )

    AVAILABILITY_CHOICES = (
        ('available', 'Available'),
        ('out of stock', 'Out of Stock'),
        ('running low', 'Running Low'),
    )

    color = models.CharField(max_length = 100, choices = PAINT_CHOICES, default = 'red')
    availability = models.CharField(max_length = 100, choices = AVAILABILITY_CHOICES, default = 'available')
    inventory = models.IntegerField()


    def __str__(self):
        return self.color
