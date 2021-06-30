from django.db import models

class AssetCommonInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_added = models.DateTimeField()

    class Meta:
        abstract = True

class AssetGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(AssetGroup, self).save(*args, **kwargs)

network_status_choices = [
    ('No Status', 'No Status'),
    ('Normal', 'Normal'),
    ('Disabled', 'Disabled'),
    ('Unknown', 'Unknown'),
    ('Warning', 'Warning'),
    ('Minor', 'Minor'),
    ('Major', 'Major'),
    ('Critical', 'Critical'),
    ]

device_status_choices = [
    ('In Use', 'In Use'),
    ('Installed', 'Installed'),
    ('Retired', 'Retired'),
    ('Missing', 'Missing'),
    ('Returned', 'Returned'),
    ]

class NetworkDevice(AssetCommonInfo):
    group = models.ManyToManyField(AssetGroup)
    hostname = models.CharField(max_length=100, blank=True, null=True)
    asset_code = models.CharField(max_length=100, blank=True, null=True, unique=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    network_status = models.CharField(max_length=15, choices =network_status_choices, blank=True, null=True)
    status = models.CharField(max_length=15, choices =device_status_choices, blank=True, null=True)

    def __str__(self):
        return self.name