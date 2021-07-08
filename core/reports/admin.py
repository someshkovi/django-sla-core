from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import SlaPoint, SlaAchievedOverview, DeviceDailyReportStatus
# from django.db.models import Avg

@admin.register(SlaPoint)
class SlaPointAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in SlaPoint._meta.fields if field.name != "id"]
    pass

# @admin.register(SlaPoint)
# class SlaPointAdmin(admin.ModelAdmin):
#     list_display = ("slaPoint", 'show_average')

#     def show_average(self, obj):
#         result = SlaAchievedOverview.objects.filter(slaPoint=obj).aggregate(Avg("valueWithExclusion"))
#         return result["valueWithExclusion__avg"]

@admin.register(SlaAchievedOverview)
class SlaAchievedOverviewAdmin(ImportExportModelAdmin):
    list_display = ("slaPoint", 'date', 'valueWithoutExclusion','valueWithExclusion')
    list_filter = ("slaPoint", 'date')

@admin.register(DeviceDailyReportStatus)
class DeviceDailyReportStatusAdmin(ImportExportModelAdmin):
    list_display = ['device','status', 'date']
    list_filter = ("status", 'date')
    search_fields = ('device__contains', )
    
    class Meta:
        model = DeviceDailyReportStatus