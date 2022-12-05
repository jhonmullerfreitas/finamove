from django.contrib import admin
from .models import Movement

class MovementAdmin(Movement):
    fields = ("id", "registered_at", "document")
    readonly_fields = ("id", "registered_at")


admin.site.register(MovementAdmin)


