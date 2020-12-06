from django.contrib import admin

# Register your models here.



from .models import Universities,Departments,Batches


@admin.register(Universities)
class Universities_Admin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "domain_name",
    )

@admin.register(Departments)
class Departments_Admin(admin.ModelAdmin):
    list_display = (
        "full_name",
    )

@admin.register(Batches)
class Batches_Admin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    
    #list_filter = ("provider",)
