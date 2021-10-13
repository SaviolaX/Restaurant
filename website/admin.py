from django.contrib import admin
from .models import Food, Gallery, Reservation

# Register your models here.

admin.site.register(Food)
admin.site.register(Gallery)
admin.site.register(Reservation)