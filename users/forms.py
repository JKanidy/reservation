from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'passwordП')

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    password1 = forms.CharField(label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}), required=False)
    last_name = forms.CharField(label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}), required=False)
    username = forms.CharField(label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя', 'readonly': True}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')