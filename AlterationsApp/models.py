from django.conf import settings
from django.db import models

# Create your models here.

# This is where we create the classes for our database
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('ready', 'Ready for pickup'),
        ('complete', 'Complete'),
        ('cancelled', 'Cancelled'),
    ]

    customer_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    item = models.CharField(max_length=100)
    alteration_type = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    description = models.TextField()

    status = models.CharField(max_length=25, choices=STATUS_CHOICES)

    # measurements
    chest = models.FloatField()
    waist = models.FloatField()
    hips = models.FloatField()
    inseam = models.FloatField()

    def __str__(self):
        return f"{self.id} - {self.customer_name} - {self.item}"