from django.db import models

# Create your models here.

class UsersInfo(models.Model):
    email = models.EmailField(null=True)
    user_name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)


class Computers(models.Model):
    availability_status = models.BooleanField(default=True)

class Reservations(models.Model):
    user_id = models.ForeignKey(UsersInfo, on_delete=models.CASCADE)
    computer_id = models.ForeignKey(Computers, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()

