from django.urls import path
from .views import ( PatientsListView, 
                    PatientInfoView, 
                    HomeView, 
                    PatientCreateView, 
                    PatientUpdateView,
                    PatientDeleteView,
                    AdmissionFormView,
                    AnesthesiaFormView,
                    BillsFormView,
                    SurgeryReportFormView,
                    Pagination,
                    searchbar,
                    # PaymentStatus,
                    paid,
                    # Paid,
                    report_searchbar,
                    report_pagination,
                    # checkbox,
                    export_excel,


                    InsuranceListView, 
                    InsuranceInfoView,  
                    InsuranceDeleteView,
                    InsuranceCreate,
                    # InsuranceUpdate,
                    MedicalUpdateView,
                    insurance_filter,
                    InsuranceUpdateView,
                    insurance_searchbar,
                    insurance_letter,



                    TariffInfoView,
                    TariffListView,
                    TariffCreateView,
                    TariffUpdateView,
                    TariffDeleteView,
                    # GeneratePdf,
                    # ReportResultView,
)


urlpatterns = [
    path('patient/<int:pk>/', PatientInfoView.as_view(), name='patient_info'),
    # path('patient/<int:pk>/', PaymentStatus, name='patient_info_change'),
    path('patientslist', Pagination, name='patients_list'),
    path('new_patient/', PatientCreateView.as_view(), name='new_patient'),
    path('patient/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
    path('patient/<int:pk>/medical_edit/', MedicalUpdateView.as_view(), name='medical_edit'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
    path('', HomeView.as_view(), name='home'),
    path('page/<int:page>', Pagination, name='patients_list'),
    path('patient/<int:pk>/admission_form/', AdmissionFormView.as_view(), name='admission_form'),
    path('patient/<int:pk>/anesthesia_form/', AnesthesiaFormView.as_view(), name='anesthesia_form'),
    path('patient/<int:pk>/bills_form/', BillsFormView.as_view(), name='bills_form'),
    path('patient/<int:pk>/surgery_report_form/', SurgeryReportFormView.as_view(), name='surgery_report_form'),
    path('search/', searchbar, name='search'),
    path('patient/<int:pk>/paid/', paid, name='paid'),
    path('reportsearch/', report_searchbar, name='report_search'),
    path('reports', report_pagination, name='reports'),
    # path('insurance/<slug:pk>/patients/', checkbox, name='checkbox'),
    path('export_excel', export_excel, name='export_excel'),
    path('insurance_search/', insurance_searchbar, name='insurance_search'),
    path('insurance_letter/', insurance_letter, name='insurance_letter'),

    # path('export', ReportResultView.as_view(), name='export'),
    



    path('insurance/<slug:pk>/', InsuranceInfoView.as_view(), name='insurance_info'),
    path('insurancelist', InsuranceListView.as_view(), name='insurance_list'),
    path('new_insurance/', InsuranceCreate, name='new_insurance'),
    path('insurance/<slug:pk>/edit/', InsuranceUpdateView.as_view(), name='insurance_edit'),
    path('insurance/<slug:pk>/delete/', InsuranceDeleteView.as_view(), name='insurance_delete'),
    path('insurance/<slug:pk>/patients/', insurance_filter, name='patient_insurance'),


    path('tariff/<slug:pk>/', TariffInfoView.as_view(), name='tariff_info'),
    path('tarifflist', TariffListView.as_view(), name='tariff_list'),
    path('new_tariff/', TariffCreateView.as_view(), name='new_tarrif'),
    path('tariff/<slug:pk>/edit/', TariffUpdateView.as_view(), name='tariff_edit'),
    path('tariff/<slug:pk>/delete/', TariffDeleteView.as_view(), name='tariff_delete'),


    # path('pdf/', GeneratePdf.as_view(), name='pdf'),

]


