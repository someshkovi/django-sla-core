from django.contrib import admin
from .models import PrimaryStroageTraps, PrimaryStorageModuleStatus

@admin.register(PrimaryStorageModuleStatus)
class PrimayStorageModuelStatusAdmin(admin.ModelAdmin):
    list_display = ['storageUnit', 'storageModule', 'status']
    list_filter = ['timeNow', 'status']


@admin.register(PrimaryStroageTraps)
class PrimayStorageTraps(admin.ModelAdmin):
    list_display = ['storageUnit', 'message', 'date', 'time']
    list_filter = ['date']