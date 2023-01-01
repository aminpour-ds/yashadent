from rest_framework.renderers import TemplateHTMLRenderer
from .import views


class Index(views.DoctorViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'


class Doctors(views.DoctorViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'doctors.html'


class About(views.AboutViewSet):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'About.html'

