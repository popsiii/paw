from django.contrib import admin
from .models import Team, Person

admin.site.register(Team)
admin.site.register(Person)

# Register your models here.

from django.contrib import admin
from .models import Osoba, Stanowisko

admin.site.register(Stanowisko)
admin.site.register(Osoba)
