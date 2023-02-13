from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from .models import Patient, Insurance
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
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'] = JalaliDateField(label=('تاریخ تولد'),
            widget=AdminJalaliDateWidget
        )
        self.fields['birth_date'].required = False

        # self.fields['birth_date'] = SplitJalaliDateTimeField(label=('birth_date'), 
        #     widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        # )
        
        self.fields['date_of_admission'] = JalaliDateField(label=('تاریخ پذیرش'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['date_of_admission'].required = False

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        # self.fields['date_of_admission'] = SplitJalaliDateTimeField(label=("date_of_admission"), 
        #     widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        # )

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
