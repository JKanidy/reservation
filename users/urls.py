from django.urls import path
from users.views import login, registration, cabinet

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('cabinet/', cabinet, name='cabinet'),
]
