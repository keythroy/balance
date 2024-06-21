from django.contrib import admin
from django.apps import AppConfig

class RegisterConfig(AppConfig):
    name = 'register'
    verbose_name = 'Register'
    defaul_auto_field = 'django.db.models.AutoField'