from django.db import models

class Patient(models.Model):
    gender = models.CharField(max_length=128)
    birthdate = models.DateTimeField(blank=True, null=True)
    is_superuser = models.CharField(max_length=254, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254, null=True)
    date_updated = models.DateTimeField()
    is_staff = models.IntegerField()
    patient_id = models.CharField(max_length=254, null=True)

    class Meta:
        managed = False
        db_table = 'patient'