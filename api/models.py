from django.db import models

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