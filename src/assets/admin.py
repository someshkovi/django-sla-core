from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import AssetGroup, NetworkDevice

@admin.register(NetworkDevice)
class NetworkDeviceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'asset_code', 'status')
    list_filter = ('status', 'group')
    ordering = ('name', 'asset_code')

admin.site.register(AssetGroup)