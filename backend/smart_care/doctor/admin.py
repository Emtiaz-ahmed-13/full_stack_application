from django.contrib import admin
from . import models
# Register your models here.


class SpeciallizationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(models.Specialization,SpeciallizationAdmin)
admin.site.register(models.Designation,DesignationAdmin)
admin.site.register(models.AvailableTime)
admin.site.register(models.Doctor)
admin.site.register(models.Review)


