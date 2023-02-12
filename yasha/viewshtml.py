from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from .import views    
from .models import ServiceType
from .serializers import ServiceTypeSerializer
from .permissions import IsAdminOrReadOnly


class Index(views.DoctorViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'


class Index_EN(views.DoctorViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'yasha-en/index.html'


class Doctors(views.DoctorViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'doctors.html'


class Doctors_EN(views.DoctorViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'yasha-en/doctors.html'


class About(views.AboutViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'About.html'


class About_EN(views.AboutViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'yasha-en/About.html'


@api_view()
@permission_classes([IsAdminOrReadOnly])
def Servicetype(request, pk):
    queryset = ServiceType.objects.all()
    serializer = ServiceTypeSerializer(queryset, many=True)  
    srv_detail = queryset.get(pk=pk)
    service_detail = ServiceTypeSerializer(srv_detail)
    return render(request, 'servicetype.html', {'results' :  serializer.data, 'service_detail' : service_detail.data})


@api_view()
@permission_classes([IsAdminOrReadOnly])
def Servicetype_EN(request, pk):
    queryset = ServiceType.objects.all()
    serializer = ServiceTypeSerializer(queryset, many=True)  
    srv_detail = queryset.get(pk=pk)
    service_detail = ServiceTypeSerializer(srv_detail)
    return render(request, 'yasha-en/servicetype.html', {'results' :  serializer.data, 'service_detail' : service_detail.data})


class Partners(views.PartnersViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'partners.html'


class Partners_EN(views.PartnersViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'yasha-en/partners.html'


class Samples(views.SamplesViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'samples.html'


class Samples_EN(views.SamplesViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'yasha-en/samples.html'



# ===================================inactive ===========================================================

# class Questions(views.QuestionsViewSet):    
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'questions.html'


# class Questions_EN(views.QuestionsViewSet):    
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'yasha-en/questions.html'