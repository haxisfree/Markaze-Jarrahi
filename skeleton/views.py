from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import PatientForm
from jalali_date import datetime2jalali, date2jalali
from django.db.models import Q 
import datetime
from datetime import date, datetime

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


# def search(request):
#     if request.method == "POST":
#         from_date = request.POST['from_date']
#         to_date = request.POST['to_date']
#         searched = request.POST['searched']
#         mltsr = (Patient.objects.filter(first_name__icontains=searched) |
#             Patient.objects.filter(last_name__icontains=searched) |
#             Patient.objects.filter(national_code__icontains=searched) |
#             Patient.objects.filter(phone_number__icontains=searched) |
#             Patient.objects.filter(file_number__icontains=searched) | 
#             Patient.objects.filter(date_of_admission__gte = from_date) , 
#             Patient.objects.filter(date_of_admission__lte = to_date) )
#         return render(request, 
#                     'search.html',
#                     {'searched' : searched, 'mltsr':mltsr, "from_date" : from_date , "to_date" : to_date})
#     else:

#         return render(request, 
#                     'search.html',
#                     {})





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


