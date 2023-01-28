from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient
from django.urls import reverse_lazy

class HomeView(TemplateView):
    model = Patient
    template_name = 'home.html'


class PatientInfoView(DetailView):
    model = Patient
    template_name = 'patient_info.html'


class PatientsListView(ListView):
    model = Patient
    template_name = 'patients_list.html'


class PatientCreateView(CreateView):
    model = Patient
    template_name = 'new_patient.html'
    fields='__all__'

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient_edit.html'
    fields = '__all__'

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'delete_patient.html'
    success_url = reverse_lazy('home')


class AdmissionFormView(TemplateView):
    model = Patient
    template_name = 'admission_form.html'

class AnesthesiaFormView(TemplateView):
    model = Patient
    template_name = 'anesthesia_form.html'

class BillsFormView(TemplateView):
    model = Patient
    template_name = 'bills_form.html'

class SurgeryReportFormView(TemplateView):
    model = Patient
    template_name = 'surgery_report_form.html'
