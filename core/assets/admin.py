from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from assets.models import AssetGroup, NetworkDevice, Server, AssignmentGroup, SiteScopeMonitorCurrentStatus, Location

@admin.register(NetworkDevice)
class NetworkDeviceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'asset_code', 'status')
    list_filter = ('status', 'group')
    ordering = ('name', 'asset_code')

admin.site.register(AssetGroup)

admin.site.register(AssignmentGroup)

admin.site.register(SiteScopeMonitorCurrentStatus)

admin.site.register(Location)

@admin.register(Server)
class ServerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'ip', 'assignment_group')
    list_filter = ('assignment_group', 'os_type', 'criticality_phase', 'state')
    ordering = ('assignment_group', 'name')
    search_fields = ['name']
    fields = [
        'name','assignment_group',
        ('hostname','ip'),('vmware_name','sis_name'),
        ('environment', 'state', 'criticality_phase','hosted_on_vmware'),
        ('service', 'function', 'redundant_server'),
        ('os_type', 'os_version'),
        ('cpu_count', 'memory', 'disk_space', 'root_disk_space'),
        ('date_added')
    ]

