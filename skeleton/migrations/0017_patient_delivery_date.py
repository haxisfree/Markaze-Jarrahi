# Generated by Django 4.1.7 on 2023-02-17 14:01

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0016_delete_bar'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='delivery_date',
            field=django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ تحویل'),
        ),
    ]