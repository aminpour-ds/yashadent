from datetime import datetime
from django.contrib import admin, messages
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models
from django.utils.html import format_html
from django.urls import reverse

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['fileNumber', 'first_name', 'last_name', 'identity', 'mobile', 'insurance']
    search_fields = ['first_name__istartswith', 'last_name__istartswith', 'id__istartswith', 'identity']
    list_filter = ['referrer', 'insurance']
    list_per_page = 10
    ordering = ['id']
    
    def fileNumber(self, patient):
        return patient.id 
   
    fileNumber.short_description = 'شماره پرونده'

@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile', 'email', 'Contract']
    list_editable = ['Contract']
    list_per_page = 10
    autocomplete_fields = ['user']
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['user__first_name__istartswith', 'user__last_name__istartswith']

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cost', 'duration', 'active', 'department_id']
    list_editable = ['active']
    list_per_page = 10
