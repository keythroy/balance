from django.contrib import admin # type: ignore
from django.apps import AppConfig # type: ignore
from register.models import SignIn, Register

class RegisterConfig(AppConfig):
    name = 'register'
    verbose_name = 'Register'
    defaul_auto_field = 'django.db.models.AutoField'
    admin.site.register(Register)

class SignInConfig(AppConfig):
    name = 'register'
    verbose_name = 'SignIn'
    defaul_auto_field = 'django.db.models.AutoField'
    admin.site.register(SignIn)