from django.db import models


class AccessHistory(models.Model):
    http_host = models.TextField(null=True, blank=True)
    http_referrer = models.TextField(null=True, blank=True)
    http_user_agent = models.TextField(null=True, blank=True)
    remote_addr = models.TextField(null=True, blank=True)
    remote_host = models.TextField(null=True, blank=True)
    remote_user = models.TextField(null=True, blank=True)
    server_name = models.TextField(null=True, blank=True)
    server_port = models.TextField(null=True, blank=True)
