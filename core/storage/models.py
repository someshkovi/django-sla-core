from django.db import models

class PrimaryStroageTraps(models.Model):
    storageUnit = models.CharField(max_length=20)
    alertId = models.CharField(max_length=20, blank=True, null=True)
    trapId = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=250, blank=True, null=True)
    acknowledge = models.BooleanField(default=0)
    resolved = models.BooleanField(default=0)
    nonCritical = models.BooleanField(default=0)
    note = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Primary Storage Traps'
        verbose_name_plural = 'Primary Storage Traps'
        constraints = [
            models.UniqueConstraint(fields=['storageUnit','trapId','date', 'time', 'message'], name='unique trap')
            ]

    def __str__(self):
        return f'{self.storageUnit}, {self.date}, {self.time}, {self.message}'


class PrimaryStorageModuleStatus(models.Model):
    storage_unit_choices = [
        ('441545',1),
        ('441780',2),
    ]

    storageUnit = models.CharField(choices = storage_unit_choices, max_length=20)
    storageModule = models.CharField(max_length=20)
    timeNow = models.DateTimeField()
    dateToday = models.DateField()



    status_choices_primary = [
        (1,'noError'),
        (2,'acute'),
        (3,'serious'),
        (4,'moderate'),
        (5,'service'),
    ]

    status = models.PositiveIntegerField(choices = status_choices_primary)
    nonCritical = models.BooleanField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'Primary Storage Module status'
        verbose_name_plural = 'Primary Storage Module status'
        constraints = [
            models.UniqueConstraint(fields=['storageUnit','storageModule','timeNow'], name='unique status')
            ]

    def __str__(self):
        return f'{self.storageUnit}, {self.storageModule}, {self.timeNow}, {self.status}'

class StorageUtilSummary(models.Model):
    file_system = models.CharField(max_length=50)
    size_TB = models.FloatField()
    usage_percent = models.FloatField()
    # added_date = models.DateField('date added')
    added_time = models.DateTimeField('time added',null=True, blank=True)

    def __str__(self):
        return f'{self.file_system}, {self.usage_percent}'

class StorageTapePolicySummary(models.Model):
    classId = models.CharField(max_length=50)
    percentUsed = models.FloatField()
    mediaId = models.SmallIntegerField('Count of media')
    archive = models.SmallIntegerField()
    unavail = models.SmallIntegerField()
    added_time = models.DateTimeField('time added',null=True, blank=True)

    def __str__(self):
        return f'{self.classId}, {self.percentUsed}'