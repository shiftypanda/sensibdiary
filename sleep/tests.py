import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Sleep
# Create your tests here.


def create_sleep(sleep_date, time_went_to_sleep, time_woke_in_morning):
    """
    Create a sleep with given start time and end time in datetimeformat
    used for further testing below
    """
    return Sleep.objects.create(sleep_date=sleep_date, time_went_to_sleep=time_went_to_sleep, time_woke_in_morning=time_woke_in_morning)

class SleepModelTests(TestCase):
    def test_sleep_with_past_wake_time(self):
        """
        total_time_asleep() should  if trying to create
        a wake time that is before a sleep time
        """
        time = timezone.now()
        sleep_start = time
        sleep_end = time - datetime.timedelta(hours=1)
        past_sleep = create_sleep(time, sleep_start, sleep_end)
        self.assertIs((past_sleep.sleep_start >= past_sleep.sleep_end), False)
