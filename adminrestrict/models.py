"""
adminretrict models
"""

__author__ = "Robert Romano (rromano@gmail.com)"
__copyright__ = "Copyright 2014 Robert C. Romano"


from django.db import models


class AllowedIP(models.Model):
    """
    Represents a whitelisted IP address who can access admin pages.
    """
    ip_address = models.CharField(max_length=512)
    note = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.ip_address






