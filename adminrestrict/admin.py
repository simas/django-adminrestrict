"""
adminrestrict app model admin definitions.
"""

__author__ = "Robert Romano (rromano@gmail.com)"
__copyright__ = "Copyright 2014 Robert C. Romano"


from django.contrib import admin
from adminrestrict.models import AllowedIP


class AllowedIPAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_address', 'note',)
    search_fields = ('ip_address', 'note',)

admin.site.register(AllowedIP, AllowedIPAdmin)
