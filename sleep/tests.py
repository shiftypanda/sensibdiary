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

#Placeholder for use in comparison checks datetime.timedelta(0)


class SleepModelTests(TestCase):
    def test_check_time_went_to_sleep_is_before_time_woke_in_morning_returns_false_for_past_sleep(self):
        """
        check_time_went_to_sleep_is_before_time_woke_in_morning should
        returns False for wake time before sleep time,
        """
        time = timezone.now()
        time_went_to_sleep = time
        time_woke_in_morning = time - datetime.timedelta(hours=1)
        past_sleep = create_sleep(time, time_went_to_sleep, time_woke_in_morning)
        self.assertIs((past_sleep.check_time_went_to_sleep_is_before_time_woke_in_morning()), False)

    def test_check_time_went_to_sleep_is_before_time_woke_in_morning_returns_true_for_correct_sleep(self):
        """
        check_time_went_to_sleep_is_before_time_woke_in_morning should
        returns True if sleep time is before wake time
        """
        time = timezone.now()
        time_went_to_sleep = time
        time_woke_in_morning = time + datetime.timedelta(hours=6)
        correct_sleep = create_sleep(time, time_went_to_sleep, time_woke_in_morning)
        self.assertIs((correct_sleep.check_time_went_to_sleep_is_before_time_woke_in_morning()), True)


    def test_total_time_asleep_is_not_negative(self):
        """
        total_time_asleep should not be able to be negative,
        returning an error if it is negative.
        """
        time = timezone.now()
        time_went_to_sleep = time
        time_woke_in_morning = time - datetime.timedelta(hours=1)
        past_sleep = create_sleep(time, time_went_to_sleep, time_woke_in_morning)
        self.assertRaises(ValueError)

    def test_total_time_asleep_is_returns_positive_if_correct(self):
        """
        total_time_asleep returns positive datetime for correct sleep
        """
        time = timezone.now()
        time_went_to_sleep = time
        time_woke_in_morning = time + datetime.timedelta(hours=7)
        correct_sleep = create_sleep(time, time_went_to_sleep, time_woke_in_morning)
        self.assertIs((correct_sleep.total_time_asleep() > datetime.timedelta(0)), True)
