from django.views.generic import ListView

from app.models import AccessHistory


class AccessHistoryAPIView(ListView):
    model = AccessHistory
    template_name = 'accesshistory_list.html'

    def get(self, request, *args, **kwargs):
        allowed_fields = [f.name for f in AccessHistory._meta.fields]
        lower_cased = {key.lower(): value
                       for key, value in request.META.items()
                       if key.lower() in allowed_fields}
        AccessHistory.objects.get_or_create(**lower_cased)
        return super(AccessHistoryAPIView, self).get(request, *args, **kwargs)
