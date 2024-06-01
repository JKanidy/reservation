from django.contrib import admin

from products.models import UsersInfo, Computers, Reservations
# Register your models here.
admin.site.register(UsersInfo)
admin.site.register(Computers)
admin.site.register(Reservations)
