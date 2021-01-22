from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "finished"]
    search_fields = ["name"]
    list_filter = ["finished"]
