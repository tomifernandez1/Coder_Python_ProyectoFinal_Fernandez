from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Mascotas)
admin.site.register(Cuidadores)
admin.site.register(Reservas)

