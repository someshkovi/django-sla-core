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
    storageUnit = models.CharField(max_length=20)
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