from django.contrib import admin

# Register your models here.

from .models import Project, Assigned_Project

@admin.register(Project)
class Project_Admin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "social_user",
    )


@admin.register(Assigned_Project)
class Assigned_Project_Admin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "university",
    )


    