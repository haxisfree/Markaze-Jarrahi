#!/usr/bin/python -tt

from django.shortcuts import render, redirect


# Create your views here.

from django.views.generic import ListView, DetailView, TemplateView, View, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, Insurance, Tariff
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import PatientForm, InsuranceForm, MedicalForm, TariffForm, PaidForm
from jalali_date import datetime2jalali, date2jalali
from django.db.models import Q 
import datetime
from datetime import date, datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
import datetime
import xlwt
import re











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
        qs = qs.filter(date_of_admission__lte=date_max)

    context = {'queryset' : qs}
    
    return render(request,'search.html',context)



def insurance_searchbar_filters(request):
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
        qs = qs.filter(date_of_admission__lte=date_max)

    return qs



def insurance_searchbar(request):

    qh = request.GET.get('m')
    qs = Patient.objects.all().filter(basic_insurance_id__exact=qh)
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
        qs = qs.filter(date_of_admission__lte=date_max)

    context = {'queryset' : qs}

    return render(request,'insurance_search.html',context)


def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

def Pagination(request, page=1):
    
    patient_list = Patient.objects.all()
    
    paginator = Paginator(patient_list, 5)
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
    form_class = PatientForm

    def my_view(request):
    	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'new_patient.html'
    form_class = PatientForm
    # jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient_edit.html'
    form_class = PatientForm
    def get_success_url(self):
          patientid=self.kwargs['pk']
          return reverse_lazy('patient_info', kwargs={'pk': patientid})

class MedicalUpdateView(UpdateView):
    model = Patient
    template_name = 'medical_info_list.html'
    form_class = MedicalForm
    def get_success_url(self):
          patientid=self.kwargs['pk']
          return reverse_lazy('patient_info', kwargs={'pk': patientid})



def paid(request, pk):
    obj = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        if obj.paid == False:
            obj.paid = True
            obj.save()
        else:
            obj.paid = False
            obj.save()
        return redirect('paid', pk=pk)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def insurance_letter(request):
    
    qs = request.GET.get('n')

    y = re.findall("\[(.*?)\]", qs)
    for y in y:
        x = re.split(",", y)


    li1 = []
    li2 = []
    li3 = []
    for z in x:
        f = re.sub(r"^\s+", "", z)
        li1.append(f)
    for s in li1:
        g = re.sub(r"\s+$", "", s)
        li2.append(g)

    for r in li2:
        li3.append(r[10:-1])

    
    lis = []
    for h in li3:
        try:
            rows = Patient.objects.get(first_name__exact=h)
            lis.append(rows)
        except Exception:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    

    context = {
        "patient" : lis
        }

    return render(request, 'insurance_letter.html', context)

    

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Patient' + \
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Patient')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        'نام',
        'نام خانوادگی',
        'کد ملی',
        'تلفن همراه',
        'شماره پرونده',
        'نام پزشک',
        'بیمه پایه',
        'نوع عمل بیمار',
        'وضعیت پرداخت'
        ]

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    qs = request.GET.get('y')

    y = re.findall("\[(.*?)\]", qs)
    for y in y:
        x = re.split(",", y)


    li1 = []
    li2 = []
    li3 = []
    for z in x:
        f = re.sub(r"^\s+", "", z)
        li1.append(f)
    for s in li1:
        g = re.sub(r"\s+$", "", s)
        li2.append(g)

    for r in li2:
        li3.append(r[10:-1])

    lis = []
    for h in li3:
        rows = Patient.objects.filter(first_name__exact=h).values_list(
        'first_name',
        'last_name',
        'national_code',
        'phone_number',
        'file_number',
        'docter_name',
        'basic_insurance',
        'type_of_surgery',
        'paid'
        )
        lis.append(rows)

    for q in lis:
        for row in q:    
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response






class InsuranceUpdateView(UpdateView):
    model = Insurance
    template_name = 'insurance_edit.html'
    form_class = InsuranceForm
    def get_success_url(self):
          insuranceid=self.kwargs['pk']
          return reverse_lazy('insurance_info', kwargs={'pk': insuranceid})

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
        insurance_form = InsuranceForm(request.POST, request.FILES)
        if insurance_form.is_valid():
            insurance_form.save()
            return HttpResponseRedirect(reverse('insurance_list'))
    else:
        insurance_form = InsuranceForm()
    return render(request, 'new_insurance.html', {'iform': insurance_form})

class InsuranceUpdateView(UpdateView):
    model = Insurance
    template_name = 'insurance_edit.html'
    form_class = InsuranceForm
    def get_success_url(self):
          insuranceid=self.kwargs['pk']
          return reverse_lazy('insurance_info', kwargs={'pk': insuranceid})

def insurance_filter(request, pk):
    
    qh = request.GET.get('x')
    ps = Patient.objects.all().filter(basic_insurance_id__exact=qh)
    paginator = Paginator(ps, 3)
    page = request.GET.get('screen')
    qs = paginator.get_page(page)
    
    context = {'querys' : qs}
    
    return render(request,'patient_insurance.html',context)


class TariffListView(ListView):
    model = Tariff
    context_object_name = 'tariff_obj'
    template_name = 'tariff_list.html'

class TariffInfoView(DetailView):
    model = Tariff
    template_name = 'tariff_info.html'

class TariffCreateView(CreateView):
    model = Tariff
    template_name = 'new_tariff.html'
    form_class = TariffForm
    success_url = reverse_lazy('tariff_list')

class TariffUpdateView(UpdateView):
    model = Tariff
    template_name = 'tariff_edit.html'
    form_class = TariffForm
    success_url = reverse_lazy('tariff_list')

class TariffDeleteView(DeleteView):
    model = Tariff
    template_name = 'delete_tariff.html'
    success_url = reverse_lazy('tariff_list')



def report_pagination(request, page=1):
    
    patient_list = Patient.objects.all()
    
    paginator = Paginator(patient_list, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {
        "patient" : page_obj
        }
    return render(request, 'reports.html', context)

def report_searchbar(request):
    qs = Patient.objects.all()
    name_contains_query = request.GET.get('name search')
    national_code_search_contains_query = request.GET.get('national code search')
    file_number_search_contains_query = request.GET.get('file number search')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    docter_name_search_query = request.GET.get('docter name search')
    presenter_search_query = request.GET.get('presenter search')
    anesthesia_doctor_name_search_query = request.GET.get('anesthesia doctor name search')
    operator_search_query = request.GET.get('operator search')
    basic_insurance_search_query = request.GET.get('basic insurance search')

    qf = Insurance.objects.filter(name__icontains=basic_insurance_search_query).values()[:][0]["slug"]

    if is_valid_queryparam(name_contains_query) :
        qs = qs.filter(Q(first_name__icontains=name_contains_query)
        | Q(last_name__icontains=name_contains_query)).distinct()
    
    elif is_valid_queryparam(national_code_search_contains_query) :
        qs = qs.filter(national_code__icontains=national_code_search_contains_query)

    elif is_valid_queryparam(file_number_search_contains_query) :
        qs = qs.filter(file_number__icontains=file_number_search_contains_query)
    

    if is_valid_queryparam(docter_name_search_query):
        qs = qs.filter(docter_name__icontains=docter_name_search_query)
    
    if is_valid_queryparam(presenter_search_query):
        qs = qs.filter(presenter__icontains=presenter_search_query)

    if is_valid_queryparam(anesthesia_doctor_name_search_query):
        qs = qs.filter(anesthesia_doctor_name__icontains=anesthesia_doctor_name_search_query)
    
    if is_valid_queryparam(operator_search_query):
        qs = qs.filter(operator__icontains=operator_search_query)
    

    if is_valid_queryparam(basic_insurance_search_query):
        qs = qs.filter(basic_insurance_id__exact=qf)




    if is_valid_queryparam(date_min):
        qs = qs.filter(date_of_admission__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(date_of_admission__lte=date_max)



    context = {'queryset' : qs}

    return render(request,'report_result.html',context)






