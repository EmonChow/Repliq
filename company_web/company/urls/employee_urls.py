from django.urls import path

from company.views import employee_views as views


urlpatterns = [
	path('api/employee/all/', views.getAllEmployee),

	path('api/employee/without_pagination/', views.getAllEmployeeWithoutPagination),

	path('api/employee/<int:pk>', views.getAEmployee),

	path('api/employee/create/', views.createEmployee),

	path('api/employee/update/<int:pk>', views.updateEmployee),
	
	path('api/employee/delete/<int:pk>', views.deleteEmployee),
]