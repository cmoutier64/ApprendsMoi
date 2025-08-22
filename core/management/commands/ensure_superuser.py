import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Crée/assure un superuser à partir des variables d'environnement DJANGO_SUPERUSER_*"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "") or ""
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            self.stdout.write("DJANGO_SUPERUSER_USERNAME ou DJANGO_SUPERUSER_PASSWORD manquant — on saute.")
            return

        user, created = User.objects.get_or_create(username=username, defaults={"email": email})
        if created:
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' créé."))
        else:
            changed = False
            # on ne réinitialise PAS le mot de passe à chaque déploiement
            if not user.is_superuser or not user.is_staff:
                user.is_superuser = True
                user.is_staff = True
                changed = True
            if email and user.email != email:
                user.email = email
                changed = True
            if changed:
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' mis à jour."))
            else:
                self.stdout.write(f"Superuser '{username}' déjà présent.")
