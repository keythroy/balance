from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    blc = '::::: balance :::::'
    help = blc + ' Create a token for a user'
    def add_arguments(self, parser):
        parser.add_argument('--username', type=str)
        parser.add_argument('--password', type=str)

    def handle(self, *args, **kwargs):
        
        username = kwargs['username']
        password = kwargs['password']
        self.stdout.write(self.style.WARNING(f'::::: balance ::::: Creating User: {username}'))
        
        user = User(username=username)
        user.first_name = username
        user.set_password(password)
        user.save()
        self.stdout.write(self.style.SUCCESS(f'::::: balance ::::: User Created: {username}'))
        
        self.stdout.write(self.style.WARNING(f'::::: balance ::::: Creating a new token for {username}'))
        token = Token.objects.create(user=user)
        
        self.stdout.write(self.style.SUCCESS(f'::::: balance ::::: Token Created: {token.key}'))

# b2e1ba33f1dceaeda9d0fce0bcd3c32758e314a1