from django.shortcuts import render # type: ignore
from rest_framework.viewsets import ModelViewSet
from register.models import Register
from rest_api.serializers import RegisterSerializer

class RegisterModelViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
