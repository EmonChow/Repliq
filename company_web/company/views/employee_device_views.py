
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

from company_web.company.models import Employee, EmployeeDevice
from company_web.company.serializers import EmployeeDeviceSerializer, EmployeeSerializer


@extend_schema(
    parameters=[
        OpenApiParameter("page"),
        OpenApiParameter("size"),
    ],
    request=EmployeeDeviceSerializer,
    responses=EmployeeDeviceSerializer
)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])

def getAllEmployeeSDevice(request):
    employee_device = EmployeeDevice.objects.all()
    total_elements = employee_device.count()

    page = request.query_params.get('page')
    size = request.query_params.get('size')

    # Pagination
    # pagination = Pagination()
    # pagination.page = page
    # pagination.size = size
    # company_device = pagination.paginate_data(company_device)

    serializer = EmployeeDeviceSerializer(employee_device, many=True)

    response = {
        'employee_device': serializer.data,
        # 'page': pagination.page,
        # 'size': pagination.size,
        # 'total_pages': pagination.total_pages,
        'total_elements': total_elements,
    }

    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=EmployeeDeviceSerializer, responses=EmployeeDeviceSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])

def getAllEmployeeDeviceWithoutPagination(request):
    employee_device = EmployeeDevice.objects.all()
    serializer = EmployeeDeviceSerializer(employee_device, many=True)

    response = {
        'employee_device': serializer.data,

    }

    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=EmployeeDeviceSerializer, responses=EmployeeDeviceSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])

def getAEmployeeDevice(request, pk):
    try:
        employee = EmployeeDevice.objects.get(pk=pk)
        serializer = EmployeeDeviceSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'detail': f"Employee Device id - {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=EmployeeDeviceSerializer, responses=EmployeeDeviceSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])

def createEmployeeDevice(request):
    data = request.data
    filtered_data = {}

    for key, value in data.items():
        if value != '' and value != 0 and value != '0':
            filtered_data[key] = value

    serializer = EmployeeDeviceSerializer(data=filtered_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@extend_schema(request=EmployeeDeviceSerializer, responses=EmployeeDeviceSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])

def updateEmployeeDevice(request, pk):
    data = request.data
    filtered_data = {}

    try:
        employee_obj = EmployeeDevice.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'detail': f" Employee Device id - {pk} doesn't exists"})

    for key, value in data.items():
        if value != '' and value != '0':
            filtered_data[key] = value

    serializer = EmployeeDeviceSerializer(employee_obj, data=filtered_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)


@extend_schema(request=EmployeeDeviceSerializer, responses=EmployeeDeviceSerializer)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])

def deleteEmployeeDevice(request, pk):
    try:
        employee_device = EmployeeDevice.objects.get(pk=pk)
        employee_device.delete()
        return Response({'detail': f'Employee Device id - {pk} is deleted successfully'}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'detail': f" Employee id - {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
