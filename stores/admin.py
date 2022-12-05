from django.contrib import admin
from .models import Store
# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    fields = ("id", "name", "owner", "balance")
    readonly_fields = ("id", "name", "owner", "balance")

admin.site.register(Store, StoreAdmin)