from django.contrib import admin
from .models import Activitate,Persoana,Actiune,Domeniu,Obiect,Locatie

admin.site.register(Obiect)
admin.site.register(Domeniu)
admin.site.register(Actiune)
admin.site.register(Activitate)
admin.site.register(Persoana)
admin.site.register(Locatie)