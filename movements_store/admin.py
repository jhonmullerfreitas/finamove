from django.contrib import admin
from .models import MovementStore
# Register your models here.

class MovementStoreAdmin(admin.ModelAdmin):
    fields = ("id", "transaction_type", "date_of_currence", "transaction_value", "card", "time", "store", "doc_cnab")
    readonly_fields = ("id", "transaction_type", "date_of_currence", "transaction_value", "card", "time", "store", "doc_cnab")

admin.site.register(MovementStore, MovementStoreAdmin)