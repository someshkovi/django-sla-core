import datetime

from django.test import TestCase
from django.utils import timezone

# from django.urls import reverse

from assets.models import NetworkDevice



class NetworkDeviceTests(TestCase):

    def test_was_added_recently_with_new_asset(self):
        # returns false for assets added before 7 days
        time = timezone.now() - datetime.timedelta(days=7, seconds=1)
        old_asset = NetworkDevice(date_added=time)
        self.assertIs(old_asset.was_added_recently(), False)

    def test_was_added_recently_with_recent_question(self):
        # returns true for assets added within 7 days
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        new_asset = NetworkDevice(date_added=time)
        self.assertIs(new_asset.was_added_recently(), True)