from django.db import models

# Create your models here.

from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse
from django.core.validators import validate_comma_separated_integer_list
from django_jalali.db import models as jmodels
from django.utils.html import format_html 



class Tariff(models.Model):
    tariff = models.SlugField(primary_key=True,max_length=100, verbose_name="نام تعرفه به انگلیسی")
    kidney_crusher_cost = models.BigIntegerField(verbose_name="حق العمل سنگ شکنی", blank=True, null=True)
    anesthetic_cost = models.BigIntegerField(verbose_name="حق العمل بیهوشی", blank=True, null=True)
    drug_and_consumables_cost = models.BigIntegerField(verbose_name="هزینه دارو و لوازم مصرفی", blank=True, null=True)

    @property
    def TotalTariffWithoutMedicine(self):

        ttwm = self.kidney_crusher_cost + self.anesthetic_cost

        return ttwm


    @property
    def TotalSumForCenter(self):

        ttsfc = self.TotalTariffWithoutMedicine + self.drug_and_consumables_cost

        return ttsfc





    def __str__(self):
        return self.tariff

    def get_absolute_url(self):
        return reverse('tariff_page', args=[str(self.slug)])





class Insurance (models.Model):

    slug = models.SlugField(primary_key=True,max_length=100, verbose_name="نام انگلیسی بیمه")
    name = models.CharField(max_length=100, verbose_name="نام بیمه")
    cover = models.ImageField(upload_to='covers/' , blank=True, verbose_name="تصویر بیمه")
    franchising = models.DecimalField (max_digits = 2, decimal_places = 2, verbose_name="فرانشیز (درصد)")
    bank_account = models.CharField(max_length=100, verbose_name="بانک معرفی شده به بیمه")
    bank_card_num = models.BigIntegerField(verbose_name="شماره حساب", blank=True, null=True)
    branchs_name = models.CharField(max_length=100, verbose_name="نام شعبه")
    total_debits_and_credits = models.BigIntegerField(verbose_name="مجموع بدهکاری و بستانکاری", blank=True, null=True)


    def __str__(self):
        return self.name


    def covers(self):
        return format_html("<img width=80 height=110 style='border-radious: 5px' src='{}'>".format(self.cover.url))




    def get_absolute_url(self):
        return reverse('insurance_page', args=[str(self.slug)])


class Patient(models.Model):

    SEX_CHOICES = (
        ('M', 'مرد') , 
        ('F', 'زن'),
    )
    

    PS_CHOICES = (
        ('P', 'پزداخت شده') , 
        ('U', 'پزداخت نشده'),
    )

    INSURANCE_CHOICES = (
        ('IRAN', 'بیمه ایران') , 
        ('DANA', 'بیمه دانا'),
        ('ASIA', 'بیمه آسیا') , 
        ('SOS', 'بیمه SOS'),
        ('ALBORZ', 'بیمه البرز') , 
        ('SINA', 'بیمه سینا'),
        ('SEPAH_BANK', 'بیمه بانک سپه') , 
        ('TEJARAT_BANK', 'بیمه بانک تجارت'),
        ('KESHAVARZI_BANK', 'بیمه بانک کشاورزی') , 
        ('MELLAT', 'بیمه ملت'),
        ('MA', 'بیمه ما') , 
        ('SAMAN', 'بیمه سامان'),
        ('SARMAD', 'بیمه سرمد') , 
        ('TEJARATE NO', 'بیمه تجارت نو'),
        ('ARMAN', 'بیمه آرمان') , 
        ('TAAVON', 'بیمه تعاون'),
        ('NOVIN', 'بیمه نوین') , 
        ('SAR DAFTARAN', 'بیمه سر دفتران'),
        ('KAR AFARIN', 'بیمه کارآفرین') , 
        ('SEDA VA SIMA', 'بیمه صدا و سیما'),
        ('ATIEH SAZAN', 'بیمه آتیه سازان') , 
        ('SHAHRDARI', 'بیمه شهرداری'),
        ('15 KHORDAD', 'بیمه ۱۵ خرداد') , 
    
      )



    id = models.AutoField(primary_key=True, verbose_name="شناسه")
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=200, verbose_name="نام خانوادگی")    
    father_name = models.CharField(max_length=100, verbose_name="نام پدر", blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name="جنسیت", blank=True, null=True)    
    birth_date = models.DateTimeField(verbose_name="تاریخ تولد", blank=True, null=True)
    national_code = models.BigIntegerField(verbose_name="کد ملی", blank=True, null=True)
    phone_number = models.BigIntegerField(verbose_name="تلفن همراه", blank=True, null=True)
    home_phone = models.BigIntegerField(verbose_name="تلفن ثابت", blank=True, null=True)
    date_of_admission = jmodels.jDateTimeField(default = timezone.now, verbose_name="تاریخ پذیزش", blank=True, null=True)
    file_number = models.CharField(max_length=300, verbose_name="شماره پرونده", blank=True, null=True) 
    description = models.TextField(verbose_name="توضیحات", blank=True, null=True)
    address = models.TextField(verbose_name="آدرس منزل", blank=True, null=True)

    docter_name = models.CharField(max_length=100, verbose_name="نام پزشک معرف", blank=True, null=True)
    anesthesia_doctor_name = models.CharField(max_length=100, verbose_name="نام پزشک بیهوشی", blank=True, null=True)
    presenter = models.CharField(max_length=100, verbose_name="نام معرف", blank=True, null=True)
    operator = models.CharField(max_length=100, verbose_name="نام اپراتور سنگ شکنی", blank=True, null=True)
    basic_insurance = models.ForeignKey(Insurance, blank=True, null=True, on_delete=models.PROTECT)
    supplementary_insurance = models.CharField(max_length=100, verbose_name="بیمه تکمیلی", blank=True, null=True)
    date_of_hospitalization = models.DateTimeField(verbose_name="تاریخ بستری", blank=True, null=True)
    date_of_discharge = models.DateTimeField(verbose_name="تاریخ ترخیص", blank=True, null=True)
    type_of_surgery = models.CharField(max_length=100, verbose_name="نوع عمل", blank=True, null=True)
    payment_tariff = models.ForeignKey(Tariff, blank=True, null=True, on_delete=models.PROTECT)
    payment_status = models.CharField(max_length=1, choices=PS_CHOICES, verbose_name="وضعیت پرداخت", default="U")

    delivery_date =  jmodels.jDateTimeField(verbose_name='تاریخ تحویل', blank=True, null=True)




    @property
    def Franchise(self):

        if self.basic_insurance:
            first_tariff_object = Tariff.objects.get( tariff__exact = self.payment_tariff_id )
            f = first_tariff_object.TotalTariffWithoutMedicine * self.basic_insurance.franchising
            return int(f)
        else:
            message = "ابتدا بیمه اصلی را انتخاب کنید"
            return message


    @property
    def InsurancePremium(self):
        
        if self.Franchise == "ابتدا بیمه اصلی را انتخاب کنید" :
            message_2 = "ابتدا بیمه اصلی را انتخاب کنید"
            return message_2
        else:
            second_tariff_object = Tariff.objects.get( tariff__exact = self.payment_tariff_id )
            ip = second_tariff_object.TotalTariffWithoutMedicine - self.Franchise
            return int(ip)

            





    class Meta: 
        ordering = ['-date_of_admission']
    
    
    
    def __str__(self):
        return self.first_name


    def get_absolute_url(self):
        return reverse('patient_info', args=[str(self.id)])



    
