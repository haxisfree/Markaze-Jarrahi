from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Patient

class PatientListView(ListView):
    model = Patient
    template_name = 'home.html'


class PatientInfoView(DetailView):
    model = Patient
    template_name = 'patient_info.html'

