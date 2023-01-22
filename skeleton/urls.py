from django.urls import path
from .views import PatientsListView, PatientInfoView, HomeView


urlpatterns = [
    path('patient/<int:pk>/', PatientInfoView.as_view(), name='patient_info'),
    path('patientslist/', PatientsListView.as_view(), name='patients_list'),
    path('', HomeView.as_view(), name='home'),
]


