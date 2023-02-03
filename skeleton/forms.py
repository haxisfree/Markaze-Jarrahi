from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from .models import Patient


class DateInput(forms.DateInput):
    input_type = 'date'


class PatientForm(ModelForm):

    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {
            'birth_date': DateInput(),
            "date_of_admission": DateInput(),
        }