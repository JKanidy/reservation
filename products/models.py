from django.db import models

from users.models import User


# Create your models here.

#class UsersInfo(models.Model):
 #   email = models.EmailField(null=True)
 #   user_name = models.CharField(max_length=128)
  #  password = models.CharField(max_length=128)
 #   def __str__(self):
   #     return self.user_name


class Computers(models.Model):
    computer_name = models.CharField(max_length=128)
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return self.computer_name


class Reservations(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    computer_id = models.ForeignKey(to=Computers, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пользователь: {self.user_id} | Компьютер #: {self.computer_id}'
