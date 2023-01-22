from django.db import models

# Create your models here.

from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse


class Patient(models.Model):

    SEX_CHOICES = (
        ('M', 'Male') , 
        ('F', 'Female')
    )

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)    
    father_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)    
    birth_date = models.DateTimeField()
    national_code = models.BigIntegerField()
    phone_number = models.BigIntegerField()
    home_phone = models.BigIntegerField()
    date_of_admission = models.DateTimeField(default = timezone.now)
    file_number = models.CharField(max_length=300) 
    docter_name = models.CharField(max_length=100)
    description = models.TextField()
    
    
    
    def __str__(self):
        return self.first_name


    def get_absolute_url(self):
        return reverse('patient_info', args=[str(self.id)])

