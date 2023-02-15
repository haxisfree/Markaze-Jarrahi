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


                    InsuranceListView, 
                    InsuranceInfoView,  
                    InsuranceDeleteView,
                    InsuranceCreate,
                    # InsuranceUpdate,
                    MedicalUpdateView,
                    insurance_filter,
                    InsuranceUpdateView,



                    TariffInfoView,
                    TariffListView,
                    TariffCreateView,
                    TariffUpdateView,
                    TariffDeleteView,
)


urlpatterns = [
    path('patient/<int:pk>/', PatientInfoView.as_view(), name='patient_info'),
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

]


