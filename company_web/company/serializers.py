from company.models import CompanyDevice

from rest_framework import serializers

from company.models import Employee, EmployeeDevice, EmployeeDeviceLog

class CompanyDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDevice
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDevice
        fields = '__all__'   
        
class EmployeeDeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDeviceLog
        fields = '__all__'           