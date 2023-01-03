from django.urls import path, include
from rest_framework_nested import routers
from django.views.generic import TemplateView
from . import views, viewshtml


router = routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet)
router.register('services', views.ServiceViewSet)
router.register('servicetype', views.ServiceTypeViewSet)
router.register('insurance', views.InsuranceViewSet)
router.register('review', views.ReviewViewSet)
router.register('about', views.AboutViewSet, basename='about')
router.register('AppointmentRequest', views.AppointmentRequestViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

# =======================================================================================================

html_router = routers.DefaultRouter()
html_router.register('doctors', viewshtml.Doctors)
html_router.register('about', viewshtml.About, basename='about')
html_router.register('servicetype', viewshtml.servicetype)
html_router.register('', viewshtml.Index)

urlpatterns += [
    path('', include(html_router.urls)),    
    path('appointment', TemplateView.as_view(template_name='appointment.html')),
]