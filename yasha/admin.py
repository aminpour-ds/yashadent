from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from . import models
from django.urls import reverse


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
    list_display = ['last_name_fa', 'first_name_fa', 'mobile', 'email', 'Contract']
    list_editable = ['Contract']
    list_per_page = 10
    autocomplete_fields = ['user']
    list_select_related = ['user']
    ordering = ['user__last_name_fa']
    search_fields = ['user__first_name_fa__istartswith', 'user__last_name_fa__istartswith']
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
    list_display = ['name_fa', 'description_fa', 'logo']
    
    def logo(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail-admin" />')
        return ''

    logo.short_description = 'لوگو'
    logo.allow_tags = True
    class Media:
        css = {
            'all': ['adminstyle/style.css']
    }


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
    list_display = ['name_fa', 'last_update']
    inlines = [ServiceTypeImageInline]

    class Media:
        css = {
            'all': ['adminstyle/style.css']
    }


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'duration', 'active', 'department']
    list_editable = ['active']
    list_per_page = 10


class ClinicImageInline(admin.TabularInline):    
    list_display = ['name', 'image']
    readonly_fields = ['thumbnail']    
    model = models.ClinicImage
    min_num = 1
    extra = 0
    
    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail-admin" />')
        return ''


class ClinicVideoInline(admin.TabularInline):    
    list_display = ['name', 'video']
    readonly_fields = ['thumbnail']    
    model = models.ClinicVideo
    min_num = 1
    extra = 0
    
    def thumbnail(self, instance):
        if instance.video.name != '':
            return format_html(f'<video src="{instance.video.url}" class="thumbnail-admin" />')
        return ''


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):  
    inlines = [ClinicImageInline, ClinicVideoInline]  
    list_display = ['email', 'linkedin', 'instagram', 'whatsapp', 'telegram', 'phone1', 'phone2', 'country_fa', 'city_fa', 'street_fa', 'flat_fa']
    class Media:
        css = {
            'all': ['adminstyle/style.css']
    }

@admin.register(models.AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'your_problem', 'phone', 'email','description', 'date']
    ordering = ['-date']


@admin.register(models.DoctorPortfolio)
class PortfolioImageInline(admin.ModelAdmin):        
    list_display = ['doctor', 'title_fa', 'title_en', 'image_tag_before', 'image_tag_after']              
    fields = ['doctor', 'title_fa', 'title_en', 'image_before', 'image_tag_before', 'image_after', 'image_tag_after']
    readonly_fields = ['image_tag_before', 'image_tag_after']    

    def image_tag_before(self, instance):
        if instance.image_before.name != '':
            return format_html(f'<img src="{instance.image_before.url}" class="thumbnail-admin" />')
        return ''

    image_tag_before.short_description = 'تصویر قبل'
    image_tag_before.allow_tags = True    

    def image_tag_after(self, instance):
        if instance.image_after.name != '':
            return format_html(f'<img src="{instance.image_after.url}" class="thumbnail-admin" />')
        return ''

    image_tag_after.short_description = 'تصویر بعد'
    image_tag_after.allow_tags = True    

    class Media:
        css = {
            'all': ['adminstyle/style.css']
    }


class ColleagueImageInline(admin.TabularInline):
    model = models.ColleagueImage
    readonly_fields = ['thumbnail']
    min_num = 1
    extra = 0
    
    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail-admin" />')
        return ''    


@admin.register(models.Colleague)
class ColleagueAdmin(admin.ModelAdmin):
    list_display = ['last_name_fa', 'first_name_fa', 'professionalStatement_fa']
    inlines = [ColleagueImageInline]
    list_per_page = 10
    autocomplete_fields = ['user']
    list_select_related = ['user']
    ordering = ['user__last_name_fa']
    search_fields = ['user__first_name_fa__istartswith', 'user__last_name_fa__istartswith']
    

    class Media:
        css = {
            'all': ['adminstyle/style.css']
    }

# ===================================inactive ===========================================================

# @admin.register(models.Patient)
# class PatientAdmin(admin.ModelAdmin):
#     list_display = ['fileNumber', 'first_name', 'last_name', 'identity', 'mobile', 'insurance']
#     search_fields = ['first_name__istartswith', 'last_name__istartswith', 'id__istartswith', 'identity']
#     list_filter = ['referrer', 'insurance']
#     list_per_page = 10
#     ordering = ['id']
    
#     def fileNumber(self, patient):
#         return patient.id 
   
#     fileNumber.short_description = 'شماره پرونده'


# @admin.register(models.Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description', 'date']


# @admin.register(models.Questions)
# class QuestionsAdmin(admin.ModelAdmin):
#     list_display = ['question_fa', 'description_fa', 'date']
#     list_per_page = 10
#     ordering = ['-date']


# @admin.register(models.Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name_fa', 'name_en']
#     list_per_page = 10