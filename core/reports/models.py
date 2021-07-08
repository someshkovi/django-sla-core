from django.db import models
from django.db.models.deletion import CASCADE
from assets.models import NetworkDevice

class SlaPoint(models.Model):
    slaPoint = models.CharField(max_length=5)
    parameter = models.CharField(max_length=300)
    Metrics = models.CharField(max_length=15, blank=True, null=True)
    baselineMetric = models.FloatField(null=True, blank=True)
    baselinePoints = models.FloatField(null=True, blank=True)
    lowerPerfomanceMetric = models.FloatField(null=True, blank=True)
    lowerPerfomancePoints = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = 'Sla Point'
        verbose_name_plural = 'Sla Points'
        constraints = [
            models.UniqueConstraint(fields=['slaPoint'], name='slaPoint')
            ]
    def __str__(self):
        return self.slaPoint


class SlaAchievedOverview(models.Model):
    date = models.DateField()
    slaPoint = models.ForeignKey(SlaPoint, to_field='slaPoint',on_delete=models.CASCADE)
    # slaPoint = models.CharField(max_length=5)
    dateExcel = models.CharField(max_length=20, blank=True, null=True)
    deviceCount = models.IntegerField(null=True, blank=True)
    totalHours = models.FloatField(null=True, blank=True)
    maintenanceHours = models.FloatField(null=True, blank=True)
    unavailableHours = models.FloatField(null=True, blank=True)
    exclusionHours = models.FloatField(null=True, blank=True)
    valueWithoutExclusion = models.FloatField(null=True, blank=True)
    valueWithExclusion = models.FloatField(null=True, blank=True)
    note = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Sla Achieved'
        verbose_name_plural = 'Sla Achieved'
        ordering = ("date","slaPoint")
        constraints = [
            models.UniqueConstraint(fields=['date', 'slaPoint'], name='slapoint + date')
            ]

    def __str__(self):
        return f"{self.date}, {self.slaPoint}, {self.valueWithExclusion}"


current_status_choices = [
    ('No Status', 'No Status'),
    ('Normal', 'Normal'),
    ('Disabled', 'Disabled'),
    ('Unknown', 'Unknown'),
    ('Warning', 'Warning'),
    ('Minor', 'Minor'),
    ('Major', 'Major'),
    ('Critical', 'Critical'),
    ]

class DeviceDailyReportStatus(models.Model):
    device = models.ForeignKey(NetworkDevice, on_delete=CASCADE)
    status = models.CharField(max_length=15, choices=current_status_choices, default='Normal')
    issue = models.CharField(max_length=300, blank=True, null=True, default='Working')
    supportRequired = models.CharField(max_length=50, blank=True, null=True, default='Working')
    incidentNumber = models.CharField(max_length=30, blank=True, null=True)
    responsibility = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=15, blank=True, null=True)
    reason = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    aging = models.PositiveSmallIntegerField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'Device daily status'
        constraints = [
            models.UniqueConstraint(fields=['device','date'], name='device daily status duplicate entry'),
        ]
    def __str__(self):
        return u"%s status is %s at %s" %(self.device, self.status, self.date)