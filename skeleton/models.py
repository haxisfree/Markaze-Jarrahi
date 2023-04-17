from django.db import models

# Create your models here.

from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse
from django.core.validators import validate_comma_separated_integer_list
from django_jalali.db import models as jmodels
from django.utils.html import format_html 
from num2fawords import words, ordinal_words
import re
from django.core.validators import MaxValueValidator, MinValueValidator




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
    
    bank_account = models.CharField(max_length=100, verbose_name="بانک معرفی شده به بیمه", blank=True, null=True, default = '')
    bank_card_num = models.BigIntegerField(verbose_name="شماره حساب", blank=True, null=True,)
    branchs_name = models.CharField(max_length=100, verbose_name="نام شعبه", blank=True, null=True, default = '')
    total_debits_and_credits = models.BigIntegerField(verbose_name="مجموع بدهکاری و بستانکاری", blank=True, null=True)
    boss_name = models.CharField(max_length=100, verbose_name="نام مدیرعامل مرکز", blank=True, null=True, default = '')






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
    father_name = models.CharField(max_length=100, verbose_name="نام پدر", blank=True, null=True, default = '')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name="جنسیت", blank=True, null=True)    
    birth_date = jmodels.jDateField(verbose_name="تاریخ تولد", blank=True, null=True)
    national_code = models.CharField(max_length=100, verbose_name="کد ملی", blank=True, null=True, default = '')
    phone_number = models.CharField(max_length=100, verbose_name="تلفن همراه", blank=True, null=True, default = '')
    home_phone = models.CharField(max_length=100, verbose_name="تلفن ثابت", blank=True, null=True, default = '')
    date_of_admission = jmodels.jDateField(default = timezone.now, verbose_name="تاریخ پذیزش")
    file_number = models.CharField(max_length=300, verbose_name="شماره پرونده", blank=True, null=True, default = '') 
    description = models.TextField(verbose_name="توضیحات", blank=True, null=True, default = '')
    address = models.TextField(verbose_name="آدرس منزل", blank=True, null=True, default = '')

    docter_name = models.CharField(max_length=100, verbose_name="نام پزشک معرف", blank=True, null=True, default = '')
    anesthesia_doctor_name = models.CharField(max_length=100, verbose_name="نام پزشک بیهوشی", default = '')
    presenter = models.CharField(max_length=100, verbose_name="نام معرف", blank=True, null=True, default = '')
    operator = models.CharField(max_length=100, verbose_name="نام اپراتور سنگ شکنی", default = '')
    anesthesiologist = models.CharField(max_length=100, verbose_name="نام متخصص بیهوشی", blank=True, null=True, default = '')
    basic_insurance = models.ForeignKey(Insurance, on_delete=models.PROTECT)
    supplementary_insurance = models.CharField(max_length=100, verbose_name="بیمه تکمیلی", blank=True, null=True, default = '')
    date_of_hospitalization = jmodels.jDateField(verbose_name="تاریخ بستری", blank=True, null=True)
    date_of_discharge = jmodels.jDateField(verbose_name="تاریخ ترخیص", blank=True, null=True)
    type_of_surgery = models.CharField(max_length=100, verbose_name="نوع عمل", blank=True, null=True, default = '')
    payment_tariff = models.ForeignKey(Tariff, on_delete=models.PROTECT)
    paid = models.BooleanField(verbose_name="وضعیت پرداخت", default=False,blank=True, null=True)
    franchising = models.PositiveIntegerField (validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="فرانشیز (درصد)", default = 0)
    discount = models.BigIntegerField(verbose_name="تخفیف", default=0)
    canceling = models.BooleanField(verbose_name="وضعیت پذیرش", default=False)




    @property
    def FileNumber(self):

        if self.date_of_admission:
            s = str(self.date_of_admission)
            sal = re.findall("\d\d\d\d", s)
            i = self.id
            return str(sal[0]) + "_" + str(i)
        else:
            message = "ابتدا تاریخ پذیرش را انتخاب کنید"
            return message








    @property
    def Franchise(self):

        if self.franchising:
            first_tariff_object = Tariff.objects.get( tariff__exact = self.payment_tariff_id )
            f1 = first_tariff_object.TotalTariffWithoutMedicine * self.franchising / 100
            f2 = f1 - self.discount
            return int(f2)
        else:
            message = "ابتدا بیمه تکمیلی را انتخاب کنید"
            return message
    

    @property
    def InsurancePremium(self):
        
        if self.Franchise == "ابتدا بیمه تکمیلی را انتخاب کنید" :
            message_2 = "ابتدا بیمه تکمیلی را انتخاب کنید"
            return message_2
        else:
            second_tariff_object = Tariff.objects.get( tariff__exact = self.payment_tariff_id )
            ip = second_tariff_object.TotalTariffWithoutMedicine - self.Franchise - self.discount
            return int(ip)

    @property
    def InsurancePremiumFa(self):
        
        if self.Franchise != "ابتدا بیمه تکمیلی را انتخاب کنید" :
            wordnum = words(self.InsurancePremium)
            return wordnum
        else:
            message = "ابتدا بیمه تکمیلی را انتخاب کنید"
            return message


    @property
    def KidneyKruser(self):
        
        if self.payment_tariff:
            kidney = Tariff.objects.get( tariff__exact = self.payment_tariff_id )
            k = kidney.kidney_crusher_cost
            return int(k)
        else:
            message = "ابتدا تعرفه را ثبت کنید"
            return message


    
    @property
    def AnestheticCost(self):
        
        if self.payment_tariff:
            anesthetic = Tariff.objects.get( tariff__exact = self.payment_tariff_id )
            a = anesthetic.anesthetic_cost
            return int(a)
        else:
            message = "ابتدا تعرفه را ثبت کنید"
            return message

    
    @property
    def DrugCost(self):
        
        if self.payment_tariff:
            drug = Tariff.objects.get( tariff__exact = self.payment_tariff_id )
            d = drug.drug_and_consumables_cost
            return int(d)
        else:
            message = "ابتدا تعرفه را ثبت کنید"
            return message


    @property
    def Fran(self):
        
        if self.franchising:
            # fran = Patient.objects.get( slug__exact = self.basic_insurance_id )
            f = self.franchising #* 100
            return int(f)
        else:
            message = "ابتدا درصد فرانشیز بیمار را وارد کنید"
            return message

            

    # @property
    # def Fran2(self):

    #     if self.franchising:
    #         f = 100 * self.franchising
    #         return int(f)
    #     else:
    #         message = "ابتدا درصد فرانشیز بیمار را وارد کنید"
    #         return message




    @property
    def TotalSumForCenter(self):

        if self.payment_tariff:
            tar = Tariff.objects.get( tariff__exact = self.payment_tariff_id )
            d = tar.TotalSumForCenter
            return int(d)
        else:
            message = "ابتدا تعرفه را ثبت کنید"
            return message








    class Meta: 
        ordering = ['-date_of_admission']
    
    
    
    def __str__(self):
        return self.first_name


    def get_absolute_url(self):
        return reverse('discount', args=[str(self.id)])





class Fund(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="شناسه")
    title = models.CharField(max_length=100, verbose_name="عنوان", blank=True, null=True, default = '')
    description = models.TextField(verbose_name="موارد", blank=True, null=True, default = '')    
    price = models.BigIntegerField(verbose_name="قیمت", blank=True, null=True, default = '')
    date = jmodels.jDateField(default = timezone.now, verbose_name="تاریخ خرید", blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name="نام خریدار", blank=True, null=True, default = '')




    class Meta: 
        ordering = ['-date']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fund_info', args=[str(self.id)])

