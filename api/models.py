from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Patient(models.Model):
    patient_id = models.CharField(max_length=254, null=True)
    gender = models.CharField(max_length=128, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=150, null=True)
    second_name = models.CharField(max_length=150, null=True)
    surname = models.CharField(max_length=150, null=True)
    date_updated = models.DateTimeField(null=True)
    date_created = models.DateTimeField(null=True)
    voided=models.CharField(max_length=254, null=True)
    county = models.CharField(max_length=254, null=True)
    village = models.CharField(max_length=254, null=True)
    ccc_number = models.CharField(max_length=254, null=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=False)
    National_id = models.CharField(max_length=254, null=True)

class Facility(models.Model):
    name = models.CharField(max_length=254, null=True)
    mfl_code = models.CharField(max_length=128, null=True)
    facility_type = models.CharField(max_length=150, null=True)
    county = models.CharField(max_length=150, null=True)
    sub_county = models.CharField(max_length=150, null=True)
    ward = models.CharField(max_length=150, null=True)
    