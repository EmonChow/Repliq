
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
# @has_permissions([PermissionEnum.PAYMENT_METHOD_LIST.name])
def getAllCompanyDevice(request):
    company_device = CompanyDevice.objects.all()
    total_elements = company_device.count()

    page = request.query_params.get('page')
    size = request.query_params.get('size')

    # Pagination
    # pagination = Pagination()
    # pagination.page = page
    # pagination.size = size
    # company_device = pagination.paginate_data(company_device)

    serializer = CompanyDeviceSerializer(company_device, many=True)

    response = {
        'company_device': serializer.data,
        # 'page': pagination.page,
        # 'size': pagination.size,
        # 'total_pages': pagination.total_pages,
        'total_elements': total_elements,
    }

    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=CompanyDeviceSerializer, responses=CompanyDeviceSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.ATTRIBUTE_LIST.name])
def getAllCompanyDeviceWithoutPagination(request):
    company_devices = CompanyDevice.objects.all()
    serializer = CompanyDeviceSerializer(company_devices, many=True)

    response = {
        'company_devices': serializer.data,

    }

    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=CompanyDeviceSerializer, responses=CompanyDeviceSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.PAYMENT_METHOD_DETAILS.name])
def getACompanyDevice(request, pk):
    try:
        company = CompanyDevice.objects.get(pk=pk)
        serializer = CompanyDeviceSerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'detail': f"Comapny id - {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=CompanyDeviceSerializer, responses=CompanyDeviceSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.ATTRIBUTE_CREATE.name])
def createCompanyDevice(request):
    data = request.data
    filtered_data = {}

    for key, value in data.items():
        if value != '' and value != 0 and value != '0':
            filtered_data[key] = value

    serializer = CompanyDeviceSerializer(data=filtered_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@extend_schema(request=CompanyDeviceSerializer, responses=CompanyDeviceSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.ATTRIBUTE_UPDATE.name])
def updateCompanyDevice(request, pk):
    data = request.data
    filtered_data = {}

    try:
        company_device_obj = CompanyDevice.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'detail': f"Company Device id - {pk} doesn't exists"})

    for key, value in data.items():
        if value != '' and value != '0':
            filtered_data[key] = value

    serializer = CompanyDeviceSerializer(company_device_obj, data=filtered_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)


@extend_schema(request=CompanyDeviceSerializer, responses=CompanyDeviceSerializer)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.PAYMENT_METHOD_DELETE.name])
def deleteCompanyDevice(request, pk):
    try:
        company_device = CompanyDevice.objects.get(pk=pk)
        company_device.delete()
        return Response({'detail': f'Company Device id - {pk} is deleted successfully'}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'detail': f"gift id - {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
