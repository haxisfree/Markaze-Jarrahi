from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from .models import Patient, Insurance, Tariff, Fund
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime



class PatientForm(forms.ModelForm):
    

    class Meta:
        model = Patient
        fields = [
        'first_name',
        'last_name',
        'father_name',
        'sex',
        'birth_date',
        'national_code',
        'phone_number',
        'home_phone',
        'date_of_admission',
        'file_number',
        'description',
        'address',
        'docter_name',
        'presenter',
        'payment_tariff',
        'franchising',
        "anesthesia_doctor_name", 
        'operator',
        'anesthesiologist', 
        'basic_insurance', 
        'supplementary_insurance', 
        'date_of_discharge', 
        'type_of_surgery',
        ]

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'] = JalaliDateField(label=('تاریخ تولد'),
            widget=AdminJalaliDateWidget
        )
        self.fields['birth_date'].required = False
        

        self.fields['date_of_admission'] = JalaliDateField(label=('تاریخ پذیرش'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['date_of_admission'].required = False


        self.fields['date_of_hospitalization'] = JalaliDateField(label=('تاریخ بستری'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['date_of_hospitalization'].required = False
        

        self.fields['date_of_discharge'] = JalaliDateField(label=('تاریخ ترخیص'),
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['date_of_discharge'].required = False










class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = "__all__"



class MedicalForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["anesthesia_doctor_name", 'operator', 'basic_insurance', 'supplementary_insurance', 'date_of_admission', 'date_of_discharge', 'type_of_surgery','franchising', 'anesthesiologist']

    def __init__(self, *args, **kwargs):
        super(MedicalForm, self).__init__(*args, **kwargs)

        self.fields['date_of_admission'] = JalaliDateField(label=('تاریخ بستری'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['date_of_admission'].required = False
        
        self.fields['date_of_discharge'] = JalaliDateField(label=('تاریخ ترخیص'),
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['date_of_discharge'].required = False




class TariffForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = "__all__"


class PaidForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["paid"]


class CancelingForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["canceling"]

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["discount"]

class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(FundForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=('تاریخ'),
            widget=AdminJalaliDateWidget
        )
        self.fields['date'].required = False


