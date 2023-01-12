from django.contrib import admin
from . import models

admin.site.register(models.room)
admin.site.register(models.room_status)
admin.site.register(models.teacher)
admin.site.register(models.status_list)
admin.site.register(models.status)

