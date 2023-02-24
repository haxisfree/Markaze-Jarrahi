from django.contrib import admin

# Register your models here.

from .models import Patient, Insurance
from import_export import resources





class PostResources(resources.ModelResource):
    class Meta:
        model = Patient
        fields = ('first_name','last_name','birth_date','sex')
        export_order = ('first_name','last_name','birth_date','sex')




admin.site.register(Patient)
admin.site.register(Insurance)