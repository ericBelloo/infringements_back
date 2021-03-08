# Python
import pyexcel
# Django

# Rest Framework
from rest_framework import status
from rest_framework.decorators import api_view
# Models
from rest_framework.response import Response

from apps.vehicle.models import Colors, Brands, Models


MODEL_OPTIONS = {
    'color': {
        'model': Colors,
        'path': 'static/catalogs/vehicle/colors.xlsx'
    },
    'brand': {
        'model': Brands,
        'path': 'static/catalogs/vehicle/brands.xlsx'
    },
    'model': {
        'model': Models,
        'path': 'static/catalogs/vehicle/models.xlsx',
        'parent': 'brand',
        'parent_model': Brands
    },
}


@api_view(['GET'])
def process_vehicle_catalogs(request):
    model = request.GET.get('model')
    try:
        records = pyexcel.get_records(file_name=MODEL_OPTIONS[model]['path'])
    except Exception as err:
        return Response({'error': err.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    count = 0
    for item in records:
        MODEL_OPTIONS[model]['model'].objects.create(name=item['name'])
        count += 1
    return Response(
        {
            'message': f'{count} objects created'
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
def process_vehicle_catalogs_related(request):
    model = request.GET.get('model')
    try:
        records = pyexcel.get_records(file_name=MODEL_OPTIONS[model]['path'])
    except Exception as err:
        return Response(
            {'error': err.args},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    count = 0
    for item in records:
        try:
            parent_object = MODEL_OPTIONS[model]['parent_model'].objects.get(id=item['parent_id'])
        except Brands.DoesNotExist:
            raise Exception('Brand not found')
        data = {
            'name': item['name'],
            MODEL_OPTIONS[model]['parent']: parent_object,
        }
        try:
            children = MODEL_OPTIONS[model]['model'](**data)
        except Exception as err:
            return Response(
                {'error': err.args},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        children.save()
        count += 1
    return Response(
        {
            'message': f'{count} elements created'
        },
        status=status.HTTP_201_CREATED
    )
