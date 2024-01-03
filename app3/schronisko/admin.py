from django.contrib import admin

# Register your models here.
from .models import Animal
from .models import Adoption
from .models import HealthRecord
from .models import Reservation
from .models import Client


# Register your models here.
admin.site.register(Animal)
admin.site.register(HealthRecord)
admin.site.register(Adoption)
admin.site.register(Reservation)
admin.site.register(Client)
