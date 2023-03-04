from django.urls import path

from company.views import employee_device_views as views


urlpatterns = [
	path('api/employee_device/all/', views.getAllEmployeeSDevice),

	path('api/employee_device/without_pagination/', views.getAllEmployeeDeviceWithoutPagination),

	path('api/employee_device/<int:pk>', views.getAEmployeeDevice),

	path('api/employee_device/create/', views.createEmployeeDevice),

	path('api/employee_device/update/<int:pk>', views.updateEmployeeDevice),
	
	path('api/employee_device/delete/<int:pk>', views.deleteEmployeeDevice),
]