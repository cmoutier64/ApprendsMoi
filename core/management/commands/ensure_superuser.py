import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Crée un superuser si DJANGO_SUPERUSER_* sont définis"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        u = os.getenv("DJANGO_SUPERUSER_USERNAME")
        e = os.getenv("DJANGO_SUPERUSER_EMAIL", "")
        p = os.getenv("DJANGO_SUPERUSER_PASSWORD")
        if not u or not p:
            return
        if not User.objects.filter(username=u).exists():
            User.objects.create_superuser(username=u, email=e, password=p)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{u}' créé"))
