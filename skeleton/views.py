#!/usr/bin/python -tt

from django.shortcuts import render, redirect


# Create your views here.

from django.views.generic import ListView, DetailView, TemplateView, View, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, Insurance, Tariff, Fund, EPayment
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import PatientForm, InsuranceForm, MedicalForm, TariffForm, PaidForm, FundForm, DiscountForm, EPaymentForm
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
from num2fawords import words, ordinal_words
import os


#importing get_template from loader
from django.template.loader import get_template

#import render_to_pdf from util.py 
from .utils import render_to_pdf 

# from xhtml2pdf import pisa 








def is_valid_queryparam(param):
    return param != '' and param is not None


def searchbar(request):
    qs = Patient.objects.all()
    name_contains_query = request.GET.get('name search')
    family_contains_query = request.GET.get('family search')
    national_code_search_contains_query = request.GET.get('national code search')
    file_number_search_contains_query = request.GET.get('file number search')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    paid_search_query = request.GET.get('paid search')
    unpaid_search_query = request.GET.get('unpaid search')


    if is_valid_queryparam(name_contains_query) :
        qs = qs.filter(first_name__icontains=name_contains_query)
    
    elif is_valid_queryparam(family_contains_query) :
        qs = qs.filter(last_name__icontains=family_contains_query)
    
    elif is_valid_queryparam(national_code_search_contains_query) :
        qs = qs.filter(national_code__icontains=national_code_search_contains_query)

    elif is_valid_queryparam(file_number_search_contains_query) :
        qs = qs.filter(file_number__icontains=file_number_search_contains_query)
    

    if is_valid_queryparam(date_min):
        qs = qs.filter(date_of_admission__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(date_of_admission__lte=date_max)

    if paid_search_query == 'on':
        qs = qs.filter(paid=True)

    elif unpaid_search_query == 'on':
        qs = qs.filter(paid=False)

    context = {'queryset' : qs}
    
    return render(request,'search.html',context)



def insurance_searchbar_filters(request):
    qs = Patient.objects.all()
    name_contains_query = request.GET.get('name search')
    family_contains_query = request.GET.get('family search')
    national_code_search_contains_query = request.GET.get('national code search')
    file_number_search_contains_query = request.GET.get('file number search')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    paid_search_query = request.GET.get('paid search')
    unpaid_search_query = request.GET.get('unpaid search')


    if is_valid_queryparam(name_contains_query) :
        qs = qs.filter(first_name__icontains=name_contains_query)

    elif is_valid_queryparam(family_contains_query) :
        qs = qs.filter(last_name__icontains=family_contains_query)
    
    elif is_valid_queryparam(national_code_search_contains_query) :
        qs = qs.filter(national_code__icontains=national_code_search_contains_query)

    elif is_valid_queryparam(file_number_search_contains_query) :
        qs = qs.filter(file_number__icontains=file_number_search_contains_query)
    

    if is_valid_queryparam(date_min):
        qs = qs.filter(date_of_admission__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(date_of_admission__lte=date_max)


    if paid_search_query == 'on':
        qs = qs.filter(paid=True)

    elif unpaid_search_query == 'on':
        qs = qs.filter(paid=False)



    return qs



def insurance_searchbar(request):

    qh = request.GET.get('m')
    qs = Patient.objects.all().filter(basic_insurance_id__exact=qh)
    name_contains_query = request.GET.get('name search')
    family_contains_query = request.GET.get('family search')
    national_code_search_contains_query = request.GET.get('national code search')
    file_number_search_contains_query = request.GET.get('file number search')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    paid_search_query = request.GET.get('paid search')
    unpaid_search_query = request.GET.get('unpaid search')

    
    if is_valid_queryparam(name_contains_query) :
        qs = qs.filter(first_name__icontains=name_contains_query)

    elif is_valid_queryparam(family_contains_query) :
        qs = qs.filter(last_name__icontains=family_contains_query)
        
    elif is_valid_queryparam(national_code_search_contains_query) :
        qs = qs.filter(national_code__icontains=national_code_search_contains_query)

    elif is_valid_queryparam(file_number_search_contains_query) :
        qs = qs.filter(file_number__icontains=file_number_search_contains_query)
        

    if is_valid_queryparam(date_min):
        qs = qs.filter(date_of_admission__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(date_of_admission__lte=date_max)

    if paid_search_query == 'on':
        qs = qs.filter(paid=True)

    elif unpaid_search_query == 'on':
        qs = qs.filter(paid=False)

    li = []
    for q in qs:
        li.append(q.id)

    # y=type(li)

    # li2 = str(li)
    # x = re.split(",", li2)

    
    # lis = []
    # for y in x: 
    #     z=re.findall('[1-9]+', y)
    #     lis.append(z)
    
    # li1 = []
    # c = 0
    # for lig in lis:
    #     for h in lig:
    # #         # try:
    #         h2 = int(h)
    #         rows = Patient.objects.get(id__exact=h2)
    #         li1.append(rows)
    #         c += 1


    context = {'queryset' : qs, 'qid':li,}#!'x':x, 'lis':lis, 'li1':li1}

    return render(request,'insurance_search.html',context)


def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

def Pagination(request, page=1):
    
    patient_list = Patient.objects.all()
    
    paginator = Paginator(patient_list, 30)
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



class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient_edit.html'
    form_class = PatientForm
    def get_success_url(self):
          patientid=self.kwargs['pk']
          return reverse_lazy('patient_info', kwargs={'pk': patientid})




def discount(request, pk):
    obj = get_object_or_404(Patient, pk=pk)
    tar = Tariff.objects.get(tariff__exact = obj.payment_tariff_id)
    
    # tar = obj.payment_tariff_id
    context = {'patient' : obj , 'tar':tar }
    return render(request,'discount.html',context)



def dis(request, pk):
    obj = get_object_or_404(Patient, pk=pk)
    dis_value = request.POST['dis']
    if request.method == 'POST':
        if 'update' in request.POST:
            obj.discount = dis_value
            obj.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        elif 'submit' in request.POST:
            if dis_value != '' and dis_value is not None:
                obj.discount = dis_value
                obj.save()
            else:
                obj.discount = 0
                obj.save()
    return redirect('patient_info', pk=pk)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

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



def disc(request, pk):
    obj = get_object_or_404(Patient, pk=pk)
    qs = request.POST.get('disc')
    
    if request.method == 'POST':
        obj.discount == qs
        obj.save()
        return redirect('discount', pk=pk)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))









def canceling(request, pk):
    obj = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        if obj.canceling == False:
            obj.canceling = True
            obj.save()
        else:
            obj.canceling = False
            obj.save()
        return redirect('patient_info', pk=pk)

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def insurance_letter(request):
    
    qs = request.GET.get('n')
    
    
    x = re.split(",", qs)

    lis = []
    for y in x: 
        z=re.findall('[0-9]+', y)
        lis.append(z[0])
    
    lis.reverse()
    
    li1 = []
    c = 0
    for li in lis:
        # for h in li:
            try:
            # lx=int(h)
                rows = Patient.objects.get(id__exact=li)
                li1.append(rows)
                c += 1


            except Exception:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    
    
    
    k = 0
    for p in li1:
        try:
            if p.InsurancePremium is not None:
                k += p.InsurancePremium
            else:
                pass
        except:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    num = words(k)
    # num2 = ordinal_words(k)
    
    
    lis_firstid = li1[0]
    insu = Insurance.objects.get(slug__exact=lis_firstid.basic_insurance_id)

    month = {
        '-01-' : "فروردین",
        '-02-' : "اردیبهشت",
        '-03-' : "خرداد",
        '-04-' : "تیر",
        '-05-' : "مرداد",
        '-06-' : "شهریور",
        '-07-' : "مهر",
        '-08-' : "آبان",
        '-09-' : "آذر",
        '-10-' : "دی",
        '-11-' : "بهمن",
        '-12-' : "اسفند"
    }
   
    mah = ""
    sal = ""

    if lis_firstid:
        date = str(lis_firstid.date_of_admission)
        x = re.findall("\-.*\-", date)
        y = re.findall("\d\d\d\d", date)
    
    for key, value in month.items():
        try:
            if key == x[0]:
                mah = value
        except:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    sal = y[0]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # y = re.findall("\[(.*?)\]", qs)
    # for y in y:
    #     x = re.split(",", y)


    # li1 = []
    # li2 = []
    # li3 = []
    # li4 = []
    # for z in x:
    #     f = re.sub(r"^\s+", "", z)
    #     li1.append(f)
    # for s in li1:
    #     g = re.sub(r"\s+$", "", s)
    #     li2.append(g)

    # for r in li2:
    #     li3.append(r[10:-1])


    # for q in qs:
    #     li4.append(q)
    
    # lis = []
    # count = []
    # c = 0

    # for h in qslist:
        # try:
            # rows = Patient.objects.get(id__exact=h)
            # lis.append(rows)
            # c += 1
            # count.append(c)

        # except Exception:
        #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    


    # k = 0
    # for p in lis:
    #     try:
    #         if p.InsurancePremium is not None:
    #             k += p.InsurancePremium
    #         else:
    #             pass
    #     except:
    #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    # num = words(k)



    # lis_firstone = lis[0]
    # insu = Insurance.objects.get(slug__exact=lis_firstone.basic_insurance_id)

    # month = {
    #     '-01-' : "فروردین",
    #     '-02-' : "اردیبهشت",
    #     '-03-' : "خرداد",
    #     '-04-' : "تیر",
    #     '-05-' : "مرداد",
    #     '-06-' : "شهریور",
    #     '-07-' : "مهر",
    #     '-08-' : "آبان",
    #     '-09-' : "آذر",
    #     '-10-' : "دی",
    #     '-11-' : "بهمن",
    #     '-12-' : "اسفند"
    # }
   
    # mah = ""
    # sal = ""

    # if lis_firstone:
    #     date = str(lis_firstone.date_of_admission)
    #     x = re.findall("\-.*\-", date)
    #     y = re.findall("\d\d\d\d", date)
    
    # for key, value in month.items():
    #     try:
    #         if key == x[0]:
    #             mah = value
    #     except:
    #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    # sal = y[0]


 



    context = {
        "patient" : li1,
        'insurance': insu,
        "leng":c,
        "sumIP" : k,
        "numword" : num,
        "mah" : mah,
        "sal":sal,
        'qs': lis
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
        'نام پدر',
        'کد ملی',
        'تاریخ تولد',
        'جنسیت',
        'تلفن همراه',
        'تلفن منزل',
        'آدرس',
        'شماره پرونده',
        'تاریخ پذیرش',
        'نام پزشک',
        'نام پزشک بیهوشی',
        'نام اپراتور',
        "نام متخصص بیهوشی",
        'نام معرف',
        'نوع عمل',
        'بیمه تکمیلی',
        'بیمه پایه',
        'تعرفه',
        'درصد فرانشیز',
        'مبلغ فرانشیز',
        'سهم بیمار',
        'سهم بیمه',
        'جمع هزینه مرکز',
        'تعرفه سنگ شکنی',
        'تعرفه بیهوشی',
        "هزینه دارو و لوازم مصرفی",
        'هزینه تخت',
        'تخفیف',
        'وضعیت پرداخت بیمه',
        'وضعیت بیمار (کنسلی)',
        'توضیحات',
        ]

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    
    
    
    qs = request.GET.get('y')

    y = re.split(",", qs)

    lis = []
    for x in y: 
        z=re.findall('[0-9]+', x)
        lis.append(z[0])

    # y = re.findall("\[(.*?)\]", qs)
    # for y in y:
    #     x = re.split(",", y)


    # li1 = []
    # li2 = []
    # li3 = []
    # for z in x:
    #     f = re.sub(r"^\s+", "", z)
    #     li1.append(f)
    # for s in li1:
    #     g = re.sub(r"\s+$", "", s)
    #     li2.append(g)

    # for r in li2:
    #     li3.append(r[10:-1])


    lis2 = []
    for h in lis:
        # rows = Patient.objects.get(id__exact=h).values_list(
        # 'first_name',
        # 'last_name',
        # 'national_code',
        # 'phone_number',
        # 'file_number',
        # 'date_of_admission',
        # 'docter_name',
        # 'basic_insurance',
        # 'type_of_surgery',
        # 'paid',
        # 'discount',
        # #  'Franchise',
        # # 'InsurancePremium',
        # )

        lislis= []

        first_name = Patient.objects.get(id__exact=h).first_name
        lislis.append(first_name)
        last_name = Patient.objects.get(id__exact=h).last_name
        lislis.append(last_name)
        father_name = Patient.objects.get(id__exact=h).father_name
        lislis.append(father_name)
        national_code = Patient.objects.get(id__exact=h).national_code
        lislis.append(national_code)
        birth_date = Patient.objects.get(id__exact=h).birth_date
        lislis.append(birth_date)
        sex = Patient.objects.get(id__exact=h).sex
        lislis.append(sex)
        phone_number = Patient.objects.get(id__exact=h).phone_number
        lislis.append(phone_number)
        home_phone = Patient.objects.get(id__exact=h).home_phone
        lislis.append(home_phone)
        address = Patient.objects.get(id__exact=h).address
        lislis.append(address)
        file_number = Patient.objects.get(id__exact=h).file_number
        lislis.append(file_number)
        date_of_admission = Patient.objects.get(id__exact=h).date_of_admission
        lislis.append(date_of_admission)
        docter_name = Patient.objects.get(id__exact=h).docter_name
        lislis.append(docter_name)
        anesthesia_doctor_name = Patient.objects.get(id__exact=h).anesthesia_doctor_name
        lislis.append(anesthesia_doctor_name)
        operator = Patient.objects.get(id__exact=h).operator
        lislis.append(operator)
        anesthesiologist = Patient.objects.get(id__exact=h).anesthesiologist
        lislis.append(anesthesiologist)
        presenter = Patient.objects.get(id__exact=h).presenter
        lislis.append(presenter)
        type_of_surgery = Patient.objects.get(id__exact=h).type_of_surgery
        lislis.append(type_of_surgery)
        basic_insurance = Patient.objects.get(id__exact=h).basic_insurance
        lislis.append(basic_insurance)
        supplementary_insurance = Patient.objects.get(id__exact=h).supplementary_insurance
        lislis.append(supplementary_insurance)
        payment_tariff = Patient.objects.get(id__exact=h).payment_tariff
        lislis.append(payment_tariff)
        Fran = Patient.objects.get(id__exact=h).Fran
        lislis.append(Fran)
        Franchise = Patient.objects.get(id__exact=h).Franchise
        lislis.append(Franchise)
        PatientPaid = Patient.objects.get(id__exact=h).PatientPaid
        lislis.append(PatientPaid)
        InsurancePremium = Patient.objects.get(id__exact=h).InsurancePremium        
        lislis.append(InsurancePremium)
        TotalSumForCenter = Patient.objects.get(id__exact=h).TotalSumForCenter
        lislis.append(TotalSumForCenter)
        KidneyKruser = Patient.objects.get(id__exact=h).KidneyKruser
        lislis.append(KidneyKruser)
        AnestheticCost = Patient.objects.get(id__exact=h).AnestheticCost
        lislis.append(AnestheticCost)
        DrugCost = Patient.objects.get(id__exact=h).DrugCost
        lislis.append(DrugCost)
        BedCost = Patient.objects.get(id__exact=h).BedCost
        lislis.append(BedCost)
        discount = Patient.objects.get(id__exact=h).discount
        lislis.append(discount)
        paid = Patient.objects.get(id__exact=h).paid
        lislis.append(paid)
        canceling = Patient.objects.get(id__exact=h).canceling        
        lislis.append(canceling)
        description = Patient.objects.get(id__exact=h).description
        lislis.append(description)
        
        lis2.append(lislis)
        


 






        # som = []
        # F = Patient.objects.get(id__exact=h).Franchise
        # IP = Patient.objects.get(id__exact=h).InsurancePremium
        
        # rows.append(F)
        # rows.append(IP)
        







        # F = []
        # IP = []

        # for so in som:
        #     rows.append(so.Franchise) 
        #     rows.append(so.InsurancePremium) 
        
        
        
        
        
        # lis2.append(rows)




        # rows.append(F)
        # rows.append(IP)

        # tup = []
        # lili = []
        # x = list(rows)
        # for s in x:
        #     s = list(s)
        #     s[-1] = rows2
        #     s = tuple(y)
        #     tup.append(s)
        #     lili.append(tup)
    
    # lis.append(x)

        # lis2.append(rows2)
        # lis[0][-1] = rows2
    # for h2 in li3:
    #     F = h2.Franchise
    #     IP = h2.InsurancePremium
    #     lis.append(F)
    #     lis.append(IP)
        











    # qs = request.GET.get('n')
    
    
    # x = re.split(",", qs)

    # lis = []
    # for y in x: 
    #     z=re.findall('[0-9]+', y)
    #     lis.append(z[0])
    
    # li1 = []
    # c = 0
    # for li in lis:
    #     # for h in li:
    #         try:
    #         # lx=int(h)
    #             rows = Patient.objects.get(id__exact=li)
    #             li1.append(rows)
    #             c += 1


    #         except Exception:
    #             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    
    
    
    # k = 0
    # for p in li1:
    #     try:
    #         if p.InsurancePremium is not None:
    #             k += p.InsurancePremium
    #         else:
    #             pass
    #     except:
    #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




















    # for q, p in zip (lis,lis2):

        
    for q in lis2:
        # list[q]
        # q.append[p]
        # for row in q:
            
        row_num += 1
        for col_num in range(len(q)):
            ws.write(row_num, col_num, str(q[col_num]), font_style)
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

class DrugAndConsumablesFormView(DetailView):
    model = Patient
    template_name = 'drug_and_consumables_form.html'

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
    paginator = Paginator(ps, 20)
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
    
    paginator = Paginator(patient_list, 30)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {
        "patient" : page_obj
        }
    return render(request, 'reports.html', context)



def report_searchbar(request):
    qs = Patient.objects.all()
    name_contains_query = request.GET.get('name search')
    family_contains_query = request.GET.get('family search')
    national_code_search_contains_query = request.GET.get('national code search')
    file_number_search_contains_query = request.GET.get('file number search')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    docter_name_search_query = request.GET.get('docter name search')
    presenter_search_query = request.GET.get('presenter search')
    anesthesia_doctor_name_search_query = request.GET.get('anesthesia doctor name search')
    operator_search_query = request.GET.get('operator search')
    basic_insurance_search_query = request.GET.get('basic insurance search')
    paid_search_query = request.GET.get('paid search')
    unpaid_search_query = request.GET.get('unpaid search')

    qf = Insurance.objects.filter(name__icontains=basic_insurance_search_query).values()[:][0]["slug"]

    if is_valid_queryparam(name_contains_query) :
        qs = qs.filter(first_name__icontains=name_contains_query)

    elif is_valid_queryparam(family_contains_query) :
        qs = qs.filter(last_name__icontains=family_contains_query)
    
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


    if paid_search_query == 'on':
        qs = qs.filter(paid=True)

    elif unpaid_search_query == 'on':
        qs = qs.filter(paid=False)

    li = []
    for q in qs:
        li.append(q.id)

    context = {'queryset' : qs, 'qid':li}

    return render(request,'report_result.html',context)






class FundListView(ListView):
    model = Fund
    context_object_name = 'fund_obj'
    template_name = 'fund_list.html'

class FundInfoView(DetailView):
    model = Fund
    template_name = 'fund_info.html'

class FundCreateView(CreateView):
    model = Fund
    template_name = 'new_fund.html'
    form_class = FundForm
    success_url = reverse_lazy('fund_list')

class FundUpdateView(UpdateView):
    model = Fund
    template_name = 'fund_edit.html'
    form_class = FundForm
    def get_success_url(self):
          fundid=self.kwargs['pk']
          return reverse_lazy('fund_info', kwargs={'pk': fundid})

class FundDeleteView(DeleteView):
    model = Fund
    template_name = 'delete_fund.html'
    success_url = reverse_lazy('fund_list')




class SupportView(TemplateView):
    template_name = 'support.html'


# from django.core.management.base import BaseCommand

def shutdown(request):

    os.system("sudo shutdown -h +1")
    return HttpResponse(request.META.get('HTTP_REFERER'))








class EPaymentListView(ListView):
    model = EPayment
    context_object_name = 'epayment_obj'
    template_name = 'epayment_list.html'

class EPaymentInfoView(DetailView):
    model = EPayment
    template_name = 'epayment_info.html'

class EPaymentCreateView(CreateView):
    model = EPayment
    template_name = 'new_epayment.html'
    form_class = EPaymentForm
    success_url = reverse_lazy('epayment_list')

class EPaymentUpdateView(UpdateView):
    model = EPayment
    template_name = 'epayment_edit.html'
    form_class = EPaymentForm
    def get_success_url(self):
          epaymentid=self.kwargs['pk']
          return reverse_lazy('epayment_info', kwargs={'pk': epaymentid})

class EPaymentDeleteView(DeleteView):
    model = EPayment
    template_name = 'delete_epayment.html'
    success_url = reverse_lazy('epayment_list')
