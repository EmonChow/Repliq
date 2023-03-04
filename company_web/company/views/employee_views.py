
from django.core.exceptions import ObjectDoesNotExist
from commons.pagination import Pagination

from company.models import CompanyDevice
from company.serializers import CompanyDeviceSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter




from django.utils.translation import gettext_lazy as _

from company_web.company.models import Employee
from company_web.company.serializers import EmployeeSerializer


@extend_schema(
    parameters=[
        OpenApiParameter("page"),
        OpenApiParameter("size"),
    ],
    request=CompanyDeviceSerializer,
    responses=CompanyDeviceSerializer
)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])

def getAllEmployee(request):
    employee = Employee.objects.all()
    total_elements = employee.count()

    page = request.query_params.get('page')
    size = request.query_params.get('size')

    # Pagination
    pagination = Pagination()
    pagination.page = page
    pagination.size = size
    company_device = pagination.paginate_data(company_device)

    serializer = EmployeeSerializer(employee, many=True)

    response = {
        'employee': serializer.data,
        'page': pagination.page,
        'size': pagination.size,
        'total_pages': pagination.total_pages,
        'total_elements': total_elements,
    }

    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=EmployeeSerializer, responses=EmployeeSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])

def getAllEmployeeWithoutPagination(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)

    response = {
        'employee': serializer.data,

    }

    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=CompanyDeviceSerializer, responses=CompanyDeviceSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])

def getAEmployee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        serializer = CompanyDeviceSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'detail': f"Employee id - {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=EmployeeSerializer, responses=EmployeeSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])

def createEmployee(request):
    data = request.data
    filtered_data = {}

    for key, value in data.items():
        if value != '' and value != 0 and value != '0':
            filtered_data[key] = value

    serializer = EmployeeSerializer(data=filtered_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@extend_schema(request=EmployeeSerializer, responses=EmployeeSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])

def updateEmployee(request, pk):
    data = request.data
    filtered_data = {}

    try:
        employee_obj = CompanyDevice.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'detail': f" Employee Device id - {pk} doesn't exists"})

    for key, value in data.items():
        if value != '' and value != '0':
            filtered_data[key] = value

    serializer = EmployeeSerializer(employee_obj, data=filtered_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)


@extend_schema(request=EmployeeSerializer, responses=EmployeeSerializer)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])

def deleteEmployee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response({'detail': f'Employee Device id - {pk} is deleted successfully'}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'detail': f" Employee id - {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
