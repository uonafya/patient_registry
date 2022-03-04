# Generated by Django 3.2.12 on 2022-03-04 16:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_facility_county'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='date_created',
        ),
        migrations.AddField(
            model_name='patient',
            name='National_id',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='patient',
            name='sub_county',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='ward',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
