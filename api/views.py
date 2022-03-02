from django.shortcuts import render

from django.shortcuts import render

from django.core.cache import cache

from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.conf import settings
from .helpers.fetch_data import fetch_data


@api_view(['GET'])
def fetch_kenyaemr(request):
    fetch_data()
