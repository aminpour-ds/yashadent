from django.contrib import admin
from django.utils.html import format_html
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


class DoctorImageInline(admin.TabularInline):
    model = models.DoctorImage
    readonly_fields = ['thumbnail']
    min_num = 1
    extra = 0
    
    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail-admin" />')
        return ''    


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile', 'email', 'Contract']
    list_editable = ['Contract']
    list_per_page = 10
    autocomplete_fields = ['user']
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['user__first_name__istartswith', 'user__last_name__istartswith']
    inlines = [DoctorImageInline]

    class Media:
        css = {
            'all': ['adminstyle/style.css']
    }


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ServiceTypeImageInline(admin.TabularInline):
    model = models.ServiceTypeImage
    readonly_fields = ['thumbnail']
    min_num = 1
    extra = 0
    
    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail-admin" />')
        return ''    


@admin.register(models.ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'last_update']
    inlines = [ServiceTypeImageInline]

    class Media:
        css = {
            'all': ['adminstyle/style.css']
    }


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cost', 'duration', 'active', 'department']
    list_editable = ['active']
    list_per_page = 10


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date']


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['description', 'email', 'linkedin', 'instagram', 'whatsapp', 'phone1', 'phone2', 'country', 'city', 'street', 'flat']


@admin.register(models.AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'your_problem', 'phone', 'description', 'date']


@admin.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question', 'description', 'date']
