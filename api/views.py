from django.shortcuts import render
from django.core.cache import cache

from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.conf import settings
from .helpers.fetch_data import fetch_data, create_records,fetch_kmhfl_facilities
from .serializers import PatientSerializer
from .models import Patient


@api_view(['GET'])
def fetch_kenyaemr(request):
    import pdb

    kenya_emr_data = fetch_data()
    create_records(kenya_emr_data)
    pdb.set_trace()

@api_view(['GET'])
def all_patients(request):
    patients = Patient.objects.all()
    cache.set("all_patients",patients, timeout=settings.CACHE_TIME_OUT)
    serializer = PatientSerializer(patients, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def fetch_facilities(request):
    fetch_kmhfl_facilities()

