from django.urls import path

from company.views import employee_device_log_views as views


urlpatterns = [
	path('api/employee_device_log/all/', views.getAllEmployeeSDeviceLog),

	path('api/employee_device_log/without_pagination/', views.getAllEmployeeDeviceLogWithoutPagination),

	path('api/employee_device_log/<int:pk>', views.getAEmployeeDeviceLog),

	path('api/employee_device_log/create/', views.createEmployeeDeviceLog),

	path('api/employee_device_log/update/<int:pk>', views.updateEmployeeDeviceLog),
	
	path('api/employee_device_log/delete/<int:pk>', views.deleteEmployeeDeviceLog),
]