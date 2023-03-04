from django.conf import settings
from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class CompanyDevice(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="company_device")
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'CompanyDevices'
        ordering = ['-id', ]

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="employee")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="employee_user")
    role = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'Employees'
        ordering = ['-id', ]
        
    def __str__(self):
        return str(self.id)

class EmployeeDevice(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="device")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    device = models.OneToOneField(CompanyDevice, on_delete=models.CASCADE, null=True, blank=True,
                                  )
    checked_out = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'EmployeeDevices'
        ordering = ['-id', ]
        
    def __str__(self):
        return str(self.id)

class EmployeeDeviceLog(models.Model):
    log = models.CharField(max_length=255)
    employee_device = models.ForeignKey(EmployeeDevice, on_delete=models.CASCADE, null=True, blank=True, related_name="employee_deevicelog_device")
    date_created = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'EmployeeDeviceLogs'
        ordering = ['-id', ]
        
    def __str__(self):
        return str(self.id)