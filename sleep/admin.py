from django.contrib import admin

# Register your models here.
from .models import Participant, Sleep, SleepInterruption

class SleepInterruptionInline(admin.TabularInline):
    model = SleepInterruption
    extra = 1

class SleepAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,          {'fields': ['sleep_date']}),
    ('Getting to sleep', {'fields': ['time_start_preparing_for_sleep', 'time_went_into_bed']}),
    ('Actually asleep', {'fields': ['time_went_to_sleep']}),
    ('Time woke in morning', {'fields': ['time_woke_in_morning']}),
    ]
    inlines = [SleepInterruptionInline]
    list_display = ('sleep_date', 'time_start_preparing_for_sleep', 'time_went_into_bed', 'time_went_to_sleep', 'time_woke_in_morning', 'total_time_asleep')
    list_filter = ['sleep_date']
    search_fields = ['sleep_date']

admin.site.register(Sleep, SleepAdmin)
admin.site.register(Participant)
