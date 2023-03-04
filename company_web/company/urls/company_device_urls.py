from django.urls import path

from company.views import company_device_views as views


urlpatterns = [
	path('api/company_device/all/', views.getAllCompanyDevice),

	path('api/company_device/without_pagination/', views.getAllCompanyDeviceWithoutPagination),

	path('api/company_device/<int:pk>', views.getACompanyDevice),

	path('api/company_device/create/', views.createCompanyDevice),

	path('api/company_device/update/<int:pk>', views.updateCompanyDevice),
	
	path('api/company_device/delete/<int:pk>', views.deleteCompanyDevice),
]