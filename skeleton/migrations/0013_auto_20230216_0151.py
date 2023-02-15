# Generated by Django 2.2.12 on 2023-02-15 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0012_auto_20230216_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='anesthetic_cost',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='حق العمل بیهوشی'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='drug_and_consumables_cost',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='هزینه دارو و لوازم مصرفی'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='kidney_crusher_cost',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='حق العمل سنگ شکنی'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='tariff',
            field=models.SlugField(max_length=100, primary_key=True, serialize=False, verbose_name='نام تعرفه به انگلیسی'),
        ),
    ]
