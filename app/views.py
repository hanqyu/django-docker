from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import DeletionMixin

from app.models import AccessHistory


class AccessHistoryAPIView(ListView, DeletionMixin):
    model = AccessHistory
    template_name = 'accesshistory_list.html'

    def get(self, request, *args, **kwargs):
        allowed_fields = [f.name for f in AccessHistory._meta.fields]
        lower_cased = {key.lower(): value
                       for key, value in request.META.items()
                       if key.lower() in allowed_fields}
        AccessHistory.objects.get_or_create(**lower_cased)
        return super(AccessHistoryAPIView, self).get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        AccessHistory.objects.all().delete()
        return HttpResponseRedirect('/')
