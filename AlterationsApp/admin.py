from django.contrib import admin
# format for importing a new model (for making a database):
# from .models import ClassName
from .models import Order

# Register your models here.

# format for registering models:
# admin.site.register(ClassName)
admin.site.register(Order)