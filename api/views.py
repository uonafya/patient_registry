from django.shortcuts import render
from django.core.cache import cache

from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.conf import settings
from .helpers.fetch_data import fetch_data, batch_insert_patients,fetch_kmhfl_facilities
from .serializers import PatientSerializer, FacilitySerializer
from .models import Patient, Facility


@api_view(['GET'])
def fetch_kenyaemr(request):
    import pdb

    kenya_emr_data = fetch_data()
    batch_insert_patients(kenya_emr_data)
    pdb.set_trace()

@api_view(['GET'])
def all_patients(request):
    patients = Patient.objects.all()
    cache.set("all_patients",patients, timeout=settings.CACHE_TIME_OUT)
    serializer = PatientSerializer(patients, many=True)

    return_message = {
            "message": ('All patients fetched Successfully'),
            "data": serializer.data
        }
    return Response(return_message, status=status.HTTP_200_OK)

@api_view(['GET'])
def fetch_mfl_facilities(request):
    fetch_kmhfl_facilities()

    return_message = {
            "message": ('Facilities Updated Successfully'),
        }
    return Response(return_message, status=status.HTTP_200_OK)
@api_view(['GET'])
def share_facilities(request):
    facilities = Facility.objects.all()
    cache.set("facilities",facilities, timeout=settings.CACHE_TIME_OUT)
    serializer = FacilitySerializer(facilities, many=True)

    return_message = {
            # "message": ('All facilities fetched Successfully'),
            "data": serializer.data
        }
    return Response(return_message, status=status.HTTP_200_OK)

@api_view(['GET'])
def clear_cache(request):
    if request.method == 'GET':
       cache.clear()
       return_message = {
            "message": ('All Caches cleared Successfully')
        }
       return Response(return_message, status=status.HTTP_200_OK)