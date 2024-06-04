from django.contrib import admin

from products.models import Computers, Reservations
# Register your models here.

admin.site.register(Computers)
admin.site.register(Reservations)
