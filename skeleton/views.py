from django.shortcuts import render, redirect


# Create your views here.

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, Insurance
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import PatientForm, InsuranceForm, MedicalForm
from jalali_date import datetime2jalali, date2jalali
from django.db.models import Q 
import datetime
from datetime import date, datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404












def is_valid_queryparam(param):
    return param != '' and param is not None


def searchbar(request):
    qs = Patient.objects.all()
    name_contains_query = request.GET.get('name search')
    national_code_search_contains_query = request.GET.get('national code search')
    file_number_search_contains_query = request.GET.get('file number search')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')


    if is_valid_queryparam(name_contains_query) :
        qs = qs.filter(Q(first_name__icontains=name_contains_query)
        | Q(last_name__icontains=name_contains_query)).distinct()
    
    elif is_valid_queryparam(national_code_search_contains_query) :
        qs = qs.filter(national_code__icontains=national_code_search_contains_query)

    elif is_valid_queryparam(file_number_search_contains_query) :
        qs = qs.filter(file_number__icontains=file_number_search_contains_query)
    

    if is_valid_queryparam(date_min):
        qs = qs.filter(date_of_admission__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(date_of_admission__lt=date_max)



    context = {'queryset' : qs}
    return render(request, 
                    'search.html',
                    context)



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

class MedicalUpdateView(UpdateView):
    model = Patient
    template_name = 'medical_info_list.html'
    form_class = MedicalForm
    def get_success_url(self):
          patientid=self.kwargs['pk']
          return reverse_lazy('patient_info', kwargs={'pk': patientid})




class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'delete_patient.html'
    success_url = reverse_lazy('patients_list')


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


















class InsuranceInfoView(DetailView):
    model = Insurance
    template_name = 'insurance_info.html'


class InsuranceListView(ListView):
    model = Insurance
    template_name = 'insurance_list.html'
    context_object_name = 'insurance_obj'


class InsuranceDeleteView(DeleteView):
    model = Insurance
    template_name = 'delete_insurance.html'
    success_url = reverse_lazy('insurance_list')




def InsuranceCreate(request):
    if request.method == 'POST':
        insurance_form = InsuranceForm(request.POST)
        if insurance_form.is_valid():
            insurance_form.save()
            return HttpResponseRedirect(reverse('insurance_list'))
    else:
        insurance_form = InsuranceForm()
    return render(request, 'new_insurance.html', {'iform': insurance_form})


# def InsuranceUpdate( request, pk):
#     data = get_object_or_404(Insurance, slug=pk)

#     if request.method == 'POST':
#         insurance_form = InsuranceForm(instance=data)
#         if insurance_form.is_valid():
#             insurance_form.save()
#             return HttpResponseRedirect("insurance_list")
#     else:
#             insurance_form = InsuranceForm(instance=data)
        
        
#     return render(request, 'insurance_edit.html', {'inform' : insurance_form})

# class InsuranceUpdateView(UpdateView):
#     model = Patient
#     template_name = 'medical_info_list.html'
#     form_class = MedicalForm
#     def get_success_url(self):
#           patientid=self.kwargs['pk']
#           return reverse_lazy('patient_info', kwargs={'pk': patientid})


class InsuranceUpdateView(UpdateView):
    model = Insurance
    template_name = 'insurance_edit.html'
    form_class = InsuranceForm
    def get_success_url(self):
          insuranceid=self.kwargs['pk']
          return reverse_lazy('insurance_info', kwargs={'pk': insuranceid})


def insurance_filter(request, pk):
    
    qh = request.GET.get('x')
    qs = Patient.objects.all().filter(basic_insurance_id__exact=qh)

    context = {'querys' : qs}
    return render(request, 
                    'patient_insurance.html',
                    context)










