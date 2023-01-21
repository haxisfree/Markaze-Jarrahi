from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView, DetailView, TemplateView
from .models import Patient

class HomeView(TemplateView):
    model = Patient
    template_name = 'home.html'


class PatientInfoView(DetailView):
    model = Patient
    template_name = 'patient_info.html'


class PatientsListView(ListView):
    model = Patient
    template_name = 'patients_list.html'
