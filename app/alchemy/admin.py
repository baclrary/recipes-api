from django.contrib import admin

from .models import Bomb, Decotion, Oil, Potion

admin.site.register(Decotion)
admin.site.register(Potion)
admin.site.register(Oil)
admin.site.register(Bomb)
