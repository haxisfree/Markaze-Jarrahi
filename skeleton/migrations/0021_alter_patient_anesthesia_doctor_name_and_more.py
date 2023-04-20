# Generated by Django 4.1.7 on 2023-03-16 06:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0020_alter_patient_franchising'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='anesthesia_doctor_name',
            field=models.CharField(default='', max_length=100, verbose_name='نام پزشک بیهوشی'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='basic_insurance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='skeleton.insurance'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_admission',
            field=django_jalali.db.models.jDateField(default=django.utils.timezone.now, verbose_name='تاریخ پذیزش'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='operator',
            field=models.CharField(default='', max_length=100, verbose_name='نام اپراتور سنگ شکنی'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='payment_tariff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='skeleton.tariff'),
        ),
    ]