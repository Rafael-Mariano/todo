import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Things.setting')
django.setup()

from things.models import Things

def update_date():
    # obtenha os objetos do modelo
    things_objects = Things.objects.all()

    for thing in things_objects:
        # atualiza a data para refletir o novo tipo de campo
        thing.data = thing.data.date()
        thing.save()

if __name__ == "__main__":
    update_date()