from django.contrib import admin

from main.models import SiteSetting, Phone

admin.site.register(Phone)
admin.site.register(SiteSetting)
