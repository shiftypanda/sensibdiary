import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Participant(models.Model):
    login_user = models.ForeignKey ('auth.User', on_delete=models.CASCADE)
    individual_name = models.CharField (max_length=100, blank=True, null=True)
    age = models.IntegerField (blank=True, null=True)
    favourite_color = models.CharField (max_length=60, blank=True, null=True)
# TODO: Generate random unique_name that can be shared to discuss participant
    """
    def generate_unique_name(self):
        with open('/usr/share/dict/words') as f:
            words = [word.strip() for word in f]
            random_name = ' '.join(choice(words) for i in range(4))
            return random_name

    self.unique_name = generate_unique_name()
    """
    def __str__(self):
        return str(self.login_user)

class Sleep(models.Model):
    sleep_date = models.DateField('sleep date')

    time_start_preparing_for_sleep = models.DateTimeField('time started getting ready for bed', blank=True, null=True)
    time_went_into_bed = models.DateTimeField('time in bed', blank=True, null=True)
    time_went_to_sleep = models.DateTimeField('time asleep', blank=True, null=True)

    time_woke_in_morning = models.DateTimeField('time woke in morning', blank=True, null=True)


    def check_time_went_to_sleep_is_before_time_woke_in_morning(self):
        """
        Checks that time went to sleep is before waking time in the morning

        """
        # TODO: ? add value error check as well
        if self.time_woke_in_morning < self.time_went_to_sleep:
            return False
        else:
            return True
        check_time_went_to_sleep_is_before_time_woke_in_morning.boolean = True
    #TODO: Run function to check and raise error if entered incorrectly

    def total_time_asleep(self):
        """
        Calculates the total sleep time based on time went to sleep
        compared to time woke in the time woke in morning
        This does NOT include any interruptions.
        """
        # TODO: Add in calculation of sum of Sleep interruptions ? need to add time back to sleep
        if ((self.time_went_to_sleep != None) and (self.time_woke_in_morning != None)):

            wake = self.time_woke_in_morning
            sleep = self.time_went_to_sleep
            timediff = wake - sleep
            if (timediff > datetime.timedelta(0) ):
                return timediff
            else:
                return ValueError, "Time waking must be AFTER time going to sleep"
        else:
            response = "Missing data: Please make sure time went to sleep and time woke in morning are entered"
            return response

    def __str__(self):
        return str(self.sleep_date)


class SleepInterruption(models.Model):
    sleep_date = models.ForeignKey(Sleep, on_delete=models.CASCADE)

    interruption_time = models.TimeField('time woke during sleep')

    intervention = models.CharField(max_length=200)
    intervention.short_description= 'What intervention happened?'

    time_taken_to_sleep = models.IntegerField(default=10)

    # TODO: Missing variable to track total amount of time taken to get to sleep
