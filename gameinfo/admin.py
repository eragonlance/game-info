from django.contrib import admin

import gameinfo.models as models

# Register your models here.
admin.site.register(models.Platform)
admin.site.register(models.Developer)
admin.site.register(models.Publisher)
admin.site.register(models.Genre)
admin.site.register(models.Game)
admin.site.register(models.Release)
admin.site.register(models.Url)
