# Generated by Django 4.1.7 on 2023-02-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0007_remove_patient_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='paid',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='وضعیت پرداخت'),
        ),
    ]
