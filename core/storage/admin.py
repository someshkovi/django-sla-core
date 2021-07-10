from django.contrib import admin
from storage.models import PrimaryStroageTraps, PrimaryStorageModuleStatus, StorageUtilSummary, StorageTapePolicySummary

@admin.register(PrimaryStorageModuleStatus)
class PrimayStorageModuelStatusAdmin(admin.ModelAdmin):
    list_display = ['storageUnit', 'storageModule', 'status']
    list_filter = ['timeNow', 'status']


@admin.register(PrimaryStroageTraps)
class PrimayStorageTrapsAdmin(admin.ModelAdmin):
    list_display = ['storageUnit', 'message', 'date', 'time']
    list_filter = ['date']

@admin.register(StorageUtilSummary)
class StorageUtilSummaryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StorageUtilSummary._meta.fields if field.name != "id"]
    list_filter = ['added_time']

@admin.register(StorageTapePolicySummary)
class StorageTapePolicySummaryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StorageTapePolicySummary._meta.fields if field.name != "id"]
    list_filter = ['added_time']
