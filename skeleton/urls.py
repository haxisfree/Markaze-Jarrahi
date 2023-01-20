from django.urls import path
from .views import PatientListView, PatientInfoView


urlpatterns = [
    path('patient/<int:pk>/', PatientInfoView.as_view(), name='patient_info'),
    path('', PatientListView.as_view(), name='home'),
]


