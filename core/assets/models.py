import builtins
from django.core.checks.messages import Critical
from django.db import models
import datetime
from django.db.models.deletion import CASCADE
from django.utils import timezone

class AssetCommonInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class AssetGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(AssetGroup, self).save(*args, **kwargs)

location_type_choices = [
    ('Junction', 'Junction'),
    ('Viewing Center', 'Viewing Center'),
    ('CCC', 'CCC'),
    ('Data Center', 'Data Center'),
    ('Other', 'Other'),
]

commisionerate_choices = [
    ('Hyderabad','Hyderabad'),
    ('Cyberabad', 'Cyberabad'),
    ('Rachakonda', 'Rachakonda'),
]

class Location(models.Model):
    location = models.CharField(max_length=200, unique=True)
    ps_location = models.CharField(max_length=30, null=True, blank=True)
    zone_location = models.CharField(max_length=30, null=True, blank=True)
    commisionerate_location = models.CharField(max_length=30, choices=commisionerate_choices, null=True, blank=True)
    location_type = models.CharField(max_length=30,choices =location_type_choices, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.location

class AssignmentGroup(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

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
    category = models.CharField(max_length=30, null=True, blank=True)
    sub_category = models.CharField(max_length=30, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=CASCADE, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    reachability = models.BooleanField(null=True, blank=True)
    nodelaststatuschange = models.DateTimeField(null=True, blank=True)
    updated_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.date_added <=now
        # return self.date_added >=timezone.now() - datetime.timedelta(days=7)

environment_choices = [
    ('Production', 'Production'),
    ('Development', 'Development'),
    ('Test', 'Test'),
    ('Failover', 'Failover'),
]

power_status_choices = [
    ('Powered On', 'Powered On'),
    ('Powered Off', 'Powered Off')
]

criticality_phase_choices = [
    ('Non Critical Phase 1', 'Non Critical Phase 1'),
    ('Non Critical Phase 2', 'Non Critical Phase 2'),
    ('Non Critical Phase 3', 'Non Critical Phase 3'),
    ('Critical Phase 1', 'Critical Phase 1'),
    ('Critical Phase 2', 'Critical Phase 1'),
    ('Critical Phase 3', 'Critical Phase 1'),
    ('Test Phase', 'Test Phase'),
]

class Server(AssetCommonInfo):
    hostname = models.CharField(max_length=100, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    vmware_name = models.CharField(max_length=100, blank=True, null=True)
    sis_name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    assignment_group = models.ForeignKey(AssignmentGroup, on_delete=CASCADE, blank=True, null=True)
    hosted_on_vmware = models.BooleanField(default=1)
    service = models.CharField(max_length=30, blank=True, null=True)
    function = models.CharField(max_length=30, blank=True, null=True)
    environment = models.CharField(max_length=30, choices =environment_choices, blank=True, null=True)
    state = models.CharField(max_length=30, choices =power_status_choices, blank=True, null=True)
    criticality_phase = models.CharField(max_length=30, choices =criticality_phase_choices, blank=True, null=True)
    redundant_server = models.CharField(max_length=30, blank=True, null=True)
    root_disk_space = models.PositiveIntegerField(blank=True, null=True)
    os_type = models.CharField(max_length=30, blank=True, null=True)
    os_version = models.CharField(max_length=100, blank=True, null=True)
    cpu_count = models.PositiveSmallIntegerField(blank=True, null=True)
    memory = models.PositiveSmallIntegerField(blank=True, null=True)
    disk_space = models.PositiveIntegerField(blank=True, null=True)
    # ip_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SiteScopeMonitorCurrentStatus(models.Model):
    host = models.CharField(max_length=100)
    monitorName = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    monitorMetric = models.CharField(max_length=30, blank=True, null=True)
    lastUpdateTime = models.DateTimeField(blank=True, null=True)
    rstatus = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Active', null=True, blank=True)
    server = models.ForeignKey(Server, to_field='sis_name',db_constraint=False, on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        return self.monitorName