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
)


urlpatterns = [
    path('patient/<int:pk>/', PatientInfoView.as_view(), name='patient_info'),
    path('patientslist', Pagination, name='patients_list'),
    path('new_patient/', PatientCreateView.as_view(), name='new_patient'),
    path('patient/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
    path('', HomeView.as_view(), name='home'),
    path('page/<int:page>', Pagination, name='patients_list'),
    path('patient/<int:pk>/admission_form/', AdmissionFormView.as_view(), name='admission_form'),
    path('patient/<int:pk>/anesthesia_form/', AnesthesiaFormView.as_view(), name='anesthesia_form'),
    path('patient/<int:pk>/bills_form/', BillsFormView.as_view(), name='bills_form'),
    path('patient/<int:pk>/surgery_report_form/', SurgeryReportFormView.as_view(), name='surgery_report_form'),

]


