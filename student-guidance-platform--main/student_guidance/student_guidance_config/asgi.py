"""
ASGI config for student_guidance_config project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_guidance_config.settings')

application = get_asgi_application()
