# Generated by Django 4.1.7 on 2023-04-17 22:19

from django.db import migrations, models
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0021_alter_patient_anesthesia_doctor_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EPayment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='شناسه')),
                ('title', models.CharField(max_length=100, verbose_name='نام')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='توضیحات')),
                ('price', models.BigIntegerField(verbose_name='مبلغ پرداختی')),
                ('date', django_jalali.db.models.jDateField(default=django.utils.timezone.now, verbose_name='تاریخ پرداخت')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
