import os

os.environ.setdefault("DJANGO_SETINGS_MODULE", "pizzeria.settings")

import django

django.setup()

from pizzerias.models import Name

names = Name.objects.all()

for name in names:
    print(name.id, name)
