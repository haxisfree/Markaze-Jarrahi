# Generated by Django 4.1.7 on 2023-02-18 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0002_remove_patient_payments_status_patient_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='payments_status',
        ),
    ]