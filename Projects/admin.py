from django.contrib import admin

# Register your models here.

from .models import Project

@admin.register(Project)
class Project_Admin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "user",
    )