from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("first_name", "second_name","surname","dob","gender","date_updated","date_created","county","village","ccc_number")