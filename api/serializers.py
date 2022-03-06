from rest_framework import serializers
from .models import Patient, Facility

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("first_name", "second_name","surname","dob","gender","date_updated","date_created","county","village","ccc_number","mfl_code")

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ("name", "mfl_code","county","sub_county","ward","facility_type")