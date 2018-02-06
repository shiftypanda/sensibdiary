from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse


from .models import Sleep, SleepInterruption
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'sleep/index.html'
    context_object_name = 'latest_sleeps_list'

    def get_queryset(self):
        """
        Return the last seven sleeps
        """
        return Sleep.objects.filter(
        sleep_date__lte=timezone.now()
        ).order_by('-sleep_date')[:7]


class DetailView(generic.DetailView):
    model = Sleep
    template_name ='sleep/detail.html'

    def get_queryset(self):
        """
        Excludes any sleeps that haven't completed yet
        """
        return Sleep.objects.filter(sleep_date__lte=timezone.now())
