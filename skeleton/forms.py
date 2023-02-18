from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from .models import Patient, Insurance, Tariff
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

# class DateInput(forms.DateInput):
#     input_type = 'date'


# class PatientForm(ModelForm):

#     class Meta:
#         model = Patient
#         fields = "__all__"
#         widgets = {
#             'birth_date': DateInput(),
#             "date_of_admission": DateInput(),
#         }



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
         'payment_tariff']

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
        
        self.fields['delivery_date'] = JalaliDateField(label=('تاریخ تحویل'),
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['delivery_date'].required = False




# class ExampleForm(forms.Form):
#     my_date_field = forms.DateField(widget=AdminJalaliDateWidget)


# class ExampleModelForm(forms.Form):
#     class Meta:
#         widget = {'my_date_field' : DateInput()}









class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = "__all__"



class MedicalForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["anesthesia_doctor_name", 'operator', 'basic_insurance', 'supplementary_insurance', 'date_of_hospitalization', 'date_of_discharge', 'type_of_surgery']

    def __init__(self, *args, **kwargs):
        super(MedicalForm, self).__init__(*args, **kwargs)

        self.fields['date_of_hospitalization'] = JalaliDateField(label=('تاریخ بستری'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['date_of_hospitalization'].required = False
        
        self.fields['date_of_discharge'] = JalaliDateField(label=('تاریخ ترخیص'),
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['date_of_discharge'].required = False




class TariffForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = "__all__"
