from django.shortcuts import render

from django.views.generic import ListView
from notifications.models import Notification

from .models import Badassness


# Create your views here.
class BadassListView(ListView):
    model = Badassness
    paginate_by = 5
    context_object_name = 'badasses'

    template_name = 'foo/badass_list.html'

    def get_context_data(self, **kwargs):
        context = super(BadassListView, self).get_context_data(**kwargs)
        notifications = Notification.objects.all()
        context['notification'] = notifications
        context['count'] = Notification.objects.filter(unread=True).count()
        return context
