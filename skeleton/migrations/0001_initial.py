# Generated by Django 2.2.12 on 2023-01-20 09:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateTimeField()),
                ('national_code', models.BigIntegerField()),
                ('phone_number', models.BigIntegerField()),
                ('home_phone', models.BigIntegerField()),
                ('date_of_admission', models.DateTimeField(default=django.utils.timezone.now)),
                ('file_number', models.CharField(max_length=300)),
                ('docter_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
