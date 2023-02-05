from django.db import models

# Create your models here.

from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse


class Patient(models.Model):

    SEX_CHOICES = (
        ('M', 'مرد') , 
        ('F', 'زن'),
    )

    id = models.AutoField(primary_key=True, verbose_name="شناسه")
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=200, verbose_name="نام خانوادگی")    
    father_name = models.CharField(max_length=100, verbose_name="نام پدر")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name="جنسیت")    
    birth_date = models.DateTimeField(verbose_name="تاریخ تولد")
    national_code = models.BigIntegerField(verbose_name="کد ملی")
    phone_number = models.BigIntegerField(verbose_name="تلفن همراه")
    home_phone = models.BigIntegerField(verbose_name="تلفن ثابت")
    date_of_admission = models.DateTimeField(default = timezone.now, verbose_name="تاریخ پذیزش")
    file_number = models.CharField(max_length=300, verbose_name="شماره پرونده") 
    docter_name = models.CharField(max_length=100, verbose_name="نام پزشک")
    description = models.TextField(verbose_name="توضیحات")
        
    class Meta: 
        ordering = ['-date_of_admission']
    
    
    
    def __str__(self):
        return self.first_name


    def get_absolute_url(self):
        return reverse('patient_info', args=[str(self.id)])

