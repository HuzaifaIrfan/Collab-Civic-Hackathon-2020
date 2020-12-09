from django.contrib import admin

# Register your models here.

from .models import Project, Assigned_Project

@admin.register(Project)
class Project_Admin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "social_user",
        'completed',
        'project_files',
        'report',

    )
    list_filter = ("assigned_project",)


@admin.register(Assigned_Project)
class Assigned_Project_Admin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "university",
    )


    