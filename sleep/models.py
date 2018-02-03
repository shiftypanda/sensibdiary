import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Sleep(models.Model):
    sleep_date = models.DateField('sleep date')

    time_start_preparing_for_sleep = models.DateTimeField('time started getting ready for bed')
    time_went_into_bed = models.DateTimeField('time in bed')
    time_went_to_sleep = models.DateTimeField('time asleep')

    time_woke_in_morning = models.DateTimeField('time woke in morning')



    def total_time_asleep(self):
        """
        Calculates the total sleep time based on time went to sleep
        compared to time woke in the time woke in morning
        This does NOT include any interruptions.
        """
        wake = self.time_woke_in_morning
        sleep = self.time_went_to_sleep
        timediff = wake - sleep

        return timediff


class SleepInterruption(models.Model):
    sleep_date = models.ForeignKey(Sleep, on_delete=models.CASCADE)

    interruption_time = models.TimeField('time woke during sleep')

    intervention = models.CharField(max_length=200)
    intervention.short_description= 'What intervention happened?'

    time_taken_to_sleep = models.IntegerField(default=10)
