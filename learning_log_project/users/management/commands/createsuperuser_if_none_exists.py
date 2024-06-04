from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = 'Create a superuser if none exists'

    def handle(self, *args, **kwargs):
        user = get_user_model()
        if not user.objects.filter(is_superuser=True).exists():
            username = os.getenv('DJANGO_SUPERUSER_USERNAME')
            email = os.getenv('DJANGO_SUPERUSER_EMAIL')
            password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
            if username and email and password:
                user.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
            else:
                self.stdout.write(self.style.ERROR('Missing superuser credentials in environment variables.'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists.'))
