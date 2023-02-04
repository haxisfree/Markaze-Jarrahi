from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import PatientForm
from jalali_date import datetime2jalali, date2jalali


def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')



def Pagination(request, page=1):
    
    patient_list = Patient.objects.all()
    paginator = Paginator(patient_list, 1)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {
        "patient" : page_obj
        }
    return render(request, 'patients_list.html', context)

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
    # fields='__all__'
    form_class = PatientForm
    # jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient_edit.html'
    # fields = '__all__'
    form_class = PatientForm
    # jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'delete_patient.html'
    success_url = reverse_lazy('home')


class AdmissionFormView(DetailView):
    model = Patient
    template_name = 'admission_form.html'

class AnesthesiaFormView(DetailView):
    model = Patient
    template_name = 'anesthesia_form.html'

class BillsFormView(DetailView):
    model = Patient
    template_name = 'bills_form.html'

class SurgeryReportFormView(DetailView):
    model = Patient
    template_name = 'surgery_report_form.html'


