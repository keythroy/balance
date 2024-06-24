from django.contrib import admin  # type: ignore
from django.apps import AppConfig # type: ignore
from budget.models import Budget

class RegisterConfig(AppConfig):
    name = 'budget'
    verbose_name = 'Budget'
    defaul_auto_field = 'django.db.models.AutoField'
    admin.site.budget(Budget)