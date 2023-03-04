
from django.core.exceptions import ObjectDoesNotExist

from company.models import CompanyDevice
from company.serializers import CompanyDeviceSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
# from commons.pagination import Pagination



from django.utils.translation import gettext_lazy as _

from company_web.company.models import EmployeeDeviceLog
from company_web.company.serializers import EmployeeDeviceLogSerializer


@extend_schema(
    parameters=[
        OpenApiParameter("page"),
        OpenApiParameter("size"),
    ],
    request=EmployeeDeviceLogSerializer,
    responses=EmployeeDeviceLogSerializer
)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])

def getAllEmployeeSDeviceLog(request):
    employee_device_log = EmployeeDeviceLog.objects.all()
    total_elements = employee_device_log.count()

    page = request.query_params.get('page')
    size = request.query_params.get('size')

    # Pagination
    # pagination = Pagination()
    # pagination.page = page
    # pagination.size = size
    # company_device = pagination.paginate_data(company_device)

    serializer = EmployeeDeviceLogSerializer(employee_device_log, many=True)

    response = {
        'employee_device_log': serializer.data,
        # 'page': pagination.page,
        # 'size': pagination.size,
        # 'total_pages': pagination.total_pages,
        'total_elements': total_elements,
    }

    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=EmployeeDeviceLogSerializer, responses=EmployeeDeviceLogSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])

def getAllEmployeeDeviceLogWithoutPagination(request):
    employee_device_log = EmployeeDeviceLog.objects.all()
    serializer = EmployeeDeviceLogSerializer(employee_device_log, many=True)

    response = {
        'employee_device_log': serializer.data,

    }

    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=EmployeeDeviceLogSerializer, responses=EmployeeDeviceLogSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])

def getAEmployeeDeviceLog(request, pk):
    try:
        employee_device_log = EmployeeDeviceLog.objects.get(pk=pk)
        serializer = EmployeeDeviceLogSerializer(employee_device_log)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'detail': f"Employee Device Log id - {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=EmployeeDeviceLogSerializer, responses=EmployeeDeviceLogSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])

def createEmployeeDeviceLog(request):
    data = request.data
    filtered_data = {}

    for key, value in data.items():
        if value != '' and value != 0 and value != '0':
            filtered_data[key] = value

    serializer = EmployeeDeviceLogSerializer(data=filtered_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@extend_schema(request=EmployeeDeviceLogSerializer, responses=EmployeeDeviceLogSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])

def updateEmployeeDeviceLog(request, pk):
    data = request.data
    filtered_data = {}

    try:
        employee_device_log = EmployeeDeviceLog.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'detail': f" Employee Device Log id - {pk} doesn't exists"})

    for key, value in data.items():
        if value != '' and value != '0':
            filtered_data[key] = value

    serializer = EmployeeDeviceLogSerializer(employee_device_log, data=filtered_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)


@extend_schema(request=EmployeeDeviceLogSerializer, responses=EmployeeDeviceLogSerializer)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])

def deleteEmployeeDeviceLog(request, pk):
    try:
        employee_device_log = EmployeeDeviceLog.objects.get(pk=pk)
        employee_device_log.delete()
        return Response({'detail': f'Employee Device Log id - {pk} is deleted successfully'}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'detail': f" Employee id Device Log- {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
