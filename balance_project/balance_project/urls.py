"""
URL configuration for balance_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.views.generic import TemplateView # type: ignore
from django.urls import path, include # type: ignore
from register.views import register,signin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('budget/', TemplateView.as_view(template_name='budget/dashboard.html')),
    path('category/', TemplateView.as_view(template_name='category/index.html')),
    path('meta/', TemplateView.as_view(template_name='meta/index.html')),
    path('signin/', signin, name='signin'),
    path('register/', register, name='register'),
    path('', signin, name='signin'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('rest_api.urls')),
    
]
