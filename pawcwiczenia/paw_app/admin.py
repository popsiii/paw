from django.contrib import admin
from .models import Team, Person

admin.site.register(Team)
admin.site.register(Person)

# Register your models here.

from django.contrib import admin
from .models import Osoba, Stanowisko

class StanowiskoAdmin(admin.ModelAdmin) :
    list_display = ( "nazwa", "opis" )
    search_fields = ( " nazwa " , )

admin.site.register(Stanowisko, StanowiskoAdmin)


class OsobaAdmin(admin.ModelAdmin):
    list_display = ("imie","nazwisko","plec","stanowisko_z_id","data_dodania")
    fields = ("imie","nazwisko","plec","stanowisko")
    readonly_fields = ("data_dodania", )
    search_fields = ("imie", "nazwisko")
    list_filter = ("data_dodania", "stanowisko")
    

    @admin.display(description= "Stanowisko(id)")
    def stanowisko_z_id (self,obj) :
        return f"{obj.stanowisko} ({obj.stanowisko.id})"

admin.site.register(Osoba, OsobaAdmin)
