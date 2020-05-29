from __future__ import unicode_literals

import django
from django.db import models
from django.utils.translation import gettext_lazy as _

if django.VERSION[0] < 3:
    from django.utils.encoding import python_2_unicode_compatible
else:
    # noop stub
    def python_2_unicode_compatible(cls):
        return cls


@python_2_unicode_compatible
class AccessAttempt(models.Model):
    """ Access Attempt log """

    user_agent = models.CharField(verbose_name=_("User Agent"), max_length=255)
    ip_address = models.GenericIPAddressField(verbose_name=_("IP Address"), null=True)
    username = models.CharField(verbose_name=_("Username"), max_length=255, null=True)
    http_accept = models.CharField(verbose_name=_("HTTP Accept"), max_length=1025)
    path_info = models.CharField(verbose_name=_("Path"), max_length=255)
    attempt_time = models.DateTimeField(verbose_name=_("Attempt Time"), auto_now_add=True)
    login_valid = models.BooleanField(verbose_name=_("Login Valid"), default=False)

    class Meta:
        ordering = ["-attempt_time"]
        verbose_name = _("Access attempt")
        verbose_name_plural = _("Access attempts")

    def __str__(self):
        """ unicode value for this model """
        return "{0} @ {1} | {2}".format(self.username, self.attempt_time, self.login_valid)
