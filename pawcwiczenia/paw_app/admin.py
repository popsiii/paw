from django.contrib import admin
from .models import Team, Person

admin.site.register(Team)
admin.site.register(Person)

# Register your models here.

from django.contrib import admin
from .models import Osoba, Stanowisko

admin.site.register(Stanowisko)

class OsobaAdmin(admin.ModelAdmin):
    list_display = ("imie","nazwisko","plec","stanowisko","data_dodania")
    fields = ("imie","nazwisko","plec","stanowisko")

admin.site.register(Osoba, OsobaAdmin)
