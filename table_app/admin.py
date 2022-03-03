from django.contrib import admin
from . import models


@admin.register(models.TableData)
class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'quantity', 'distance')
    list_per_page = 3