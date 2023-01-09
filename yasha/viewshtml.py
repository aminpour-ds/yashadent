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


class Doctors(views.DoctorViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'doctors.html'


class About(views.AboutViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'About.html'


@api_view()
@permission_classes([IsAdminOrReadOnly])
def Servicetype(request, pk):
    queryset = ServiceType.objects.all()
    serializer = ServiceTypeSerializer(queryset, many=True)  
    srv_detail = queryset.get(pk=pk)
    service_detail = ServiceTypeSerializer(srv_detail)
    return render(request, 'servicetype.html', {'results' :  serializer.data, 'service_detail' : service_detail.data})