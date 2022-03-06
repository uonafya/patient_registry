from api.serializers import PatientSerializer
from django.core.cache import cache
from api.models import Facility
from rest_framework import serializers


def get_org_units():
    '''
    Function to fetch all Organization units from db
    Args: 
    Return: org_units()
    '''
    org_unit = {}
    if "org_unit" in cache:
        org_unit = cache.get("org_unit")
    else:
        org_unit = Facility.objects.all()
        cache.set("org_unit", org_unit)
    serializers_data = PatientSerializer(org_unit, many=True)
    return serializers_data.data