import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Create an initial admin user without replacing existing accounts'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        if not all((username, email, password)):
            raise CommandError(
                'Set DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, and '
                'DJANGO_SUPERUSER_PASSWORD to create an admin user.'
            )

        admin = User.objects.filter(username=username).first()
        if admin:
            if not admin.is_superuser:
                raise CommandError(
                    f'Username {username!r} already exists and is not a superuser.'
                )
            self.stdout.write(f'Superuser {username!r} already exists; left unchanged.')
            return

        User.objects.create_superuser(username, email, password)
        self.stdout.write(self.style.SUCCESS(f'Superuser {username!r} created.'))