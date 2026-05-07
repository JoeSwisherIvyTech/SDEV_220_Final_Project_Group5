from django.conf import settings
from django.db import models

# Create your models here.

REQUIREMENTS = {
    ('pants', 'hem'): ['inseam'],
    ('pants', 'resize'): ['waist'],
    ('dress', 'resize'): ['chest', 'waist', 'hips'],
    ('shirt', 'resize'): ['chest'],
    ('shirt', 'shorten_sleeves'): ['sleeve_length'],
    ('suit', 'resize'): ['chest', 'waist', 'shoulders'],
}
# This is where we create the classes for our database
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('ready', 'Ready for pickup'),
        ('complete', 'Complete'),
        ('cancelled', 'Cancelled'),
    ]

    ITEM_CHOICES = [
        ('dress', 'Dress'),
        ('pants', 'Pants'),
        ('shirt', 'Shirt'),
        ('skirt', 'Skirt'),
        ('suit', 'Suit'),
        ('other', 'Other')
    ]

    ALTERATION_CHOICES = [
        ('hem', 'Hem'),
        ('resize', 'Resize'),
        ('repair', 'Repair'),
        ('shorten', 'Shorten Sleeves'),
        ('take_in', 'Take In'),
        ('bust', 'Bust adjustment'),
        ('waist', 'Waist Adjustment'),
        ('hips', 'Hip Adjustment'),
        ('other', 'Other'),
    ]

    MATERIAL_CHOICES = [
        ('cotton', 'Cotton'),
        ('silk', 'Silk'),
        ('denim', 'Denim'),
        ('polyester', 'Polyester'),
        ('wool', 'Wool'),
        ('other', 'Other'),
    ]

    customer_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer')
    assigned_staff = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_staff')
    item = models.CharField(max_length=100, choices=ITEM_CHOICES)
    alteration_type = models.CharField(max_length=100, choices=ALTERATION_CHOICES)
    material = models.CharField(max_length=100, choices=MATERIAL_CHOICES)
    description = models.TextField(null=True, blank=True)
    
    

    status = models.CharField(max_length=25, choices=STATUS_CHOICES)

    # measurements
    chest = models.FloatField(null=True, blank=True)
    waist = models.FloatField(null=True, blank=True)
    hips = models.FloatField(null=True, blank=True)
    inseam = models.FloatField(null=True, blank=True)

    def assign_staff(self, staff_name):
        self.status = 'in_progress'
        self.assigned_staff = staff_name
        self.save()

    def assign_staff(self, staff_name):
        self.status = 'in_progress'
        self.assigned_staff = staff_name
        self.save()

    def __str__(self):
        return f"{self.id} - {self.customer_name} - {self.item}"