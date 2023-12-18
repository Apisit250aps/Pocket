from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'amount',
        'type'
    ]