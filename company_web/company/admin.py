from django.contrib import admin

from company.models import CompanyDevice, Employee, EmployeeDevice, EmployeeDeviceLog

# Register your models here.
@admin.register(CompanyDevice)
class CompanyDeviceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CompanyDevice._meta.fields]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]
    
    
@admin.register(EmployeeDevice)
class EmployeeDeviceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EmployeeDevice._meta.fields]    
    

@admin.register(EmployeeDeviceLog)
class EmployeeDeviceLogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EmployeeDeviceLog._meta.fields]        