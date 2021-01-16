from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Project)
admin.site.register(models.LargeText)
admin.site.register(models.SmallText)
admin.site.register(models.LargeTextSubsection)
