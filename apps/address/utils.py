
# Python
import pyexcel
# Django
from django.http import JsonResponse
# Models
from apps.address.models import States, Cities, Colonies, Postcodes


def process_postcodes(request):
    count = 0
    try:
        state = States.objects.get(name='Ciudad de México')
    except States.DoesNotExist:
        state = States.objects.create(name='Ciudad de México')
    file_path = 'static/catalogs/address/ciudad_mexico.xlsx'
    records = pyexcel.get_records(file_name=file_path)
    for item in records:
        try:
            city = Cities.objects.get(name=item['D_mnpio'])
        except Cities.DoesNotExist:
            city = Cities.objects.create(name=item['D_mnpio'], state=state)
        try:
            colony = Colonies.objects.get(name=item['d_asenta'])
        except Colonies.DoesNotExist:
            colony = Colonies.objects.create(name=item['d_asenta'], city=city)
        try:
            postcode = Postcodes.objects.get(postcode=item['d_codigo'], colony=colony)
        except Postcodes.DoesNotExist:
            postcode = Postcodes.objects.create(postcode=item['d_codigo'], colony=colony)
        if postcode:
            count += 1
    return JsonResponse({'message': f'{count} objects created'})

