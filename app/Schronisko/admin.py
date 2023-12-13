from django.contrib import admin
from .models import Zwierzak
from .models import Adopcja
from .models import HistoriaLeczenia
from .models import Rezerwacja
from .models import Klient

# Register your models here.
admin.site.register(Zwierzak)
admin.site.register(HistoriaLeczenia)
admin.site.register(Adopcja)
admin.site.register(Rezerwacja)
admin.site.register(Klient)