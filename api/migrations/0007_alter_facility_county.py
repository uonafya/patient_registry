# Generated by Django 3.2.12 on 2022-03-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_facility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='county',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
