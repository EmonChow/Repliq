
from django import views
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index),
    
    path('company/', include('company.urls.company_device_urls')),
    path('employee/', include('company.urls.employee_urls')),
    path('employee_device/', include('company.urls.employee_device_urls')),
    path('employee_device_log/', include('company.urls.employee_device_log_urls')),
]
