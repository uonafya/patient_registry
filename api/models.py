from unicodedata import name
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
    sub_county = models.CharField(max_length=254, null=True)
    ward = models.CharField(max_length=254, null=True)
    village = models.CharField(max_length=254, null=True)
    ccc_number = models.CharField(max_length=254, null=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=False)
    national_id = models.CharField(max_length=254, null=True)
    mfl_code = models.CharField(max_length=254, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.second_name, self.surname, self.ccc_number, self.national_id,self.county, self.mfl_code)

class Facility(models.Model):
    name = models.CharField(max_length=254, null=True)
    mfl_code = models.CharField(max_length=128, null=True)
    facility_type = models.CharField(max_length=150, null=True)
    county = models.CharField(max_length=150, null=True)
    sub_county = models.CharField(max_length=150, null=True)
    ward = models.CharField(max_length=150, null=True)
    # ward_id = models.CharField(max_length=150, null=True)

    def __str__(self):
        return '%s' % (self.name, self.mfl_code, self.facility_type, self.county, self.sub_county,self.ward)
    

# class County(models.Model):
#     uuid = models.CharField(max_length=254, null=True)
#     name = models.CharField(max_length=254, null=True)

# class Sub_county(models.Model):
#     uuid = models.CharField(max_length=254, null=True)
#     name = models.CharField(max_length=254, null=True)
#     county_id = models.CharField(max_length=254, null=True)

# class Ward(models.Model):
#     uuid = models.CharField(max_length=254, null=True)
#     name = models.CharField(max_length=254, null=True)
#     sub_county_id = models.CharField(max_length=254, null=True)

