import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_guidance_config.settings')

django.setup()

from django.core.management import call_command

call_command('setup_users')
