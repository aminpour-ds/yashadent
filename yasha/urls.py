from django.urls import path, include
from rest_framework_nested import routers
from django.views.generic import TemplateView
from . import views, viewshtml


router = routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet)
router.register('insurance', views.InsuranceViewSet)
router.register('review', views.ReviewViewSet)
router.register('about', views.AboutViewSet, basename='about')
router.register('AppointmentRequest', views.AppointmentRequestViewSet)

urlpatterns = [
    path('api/service/', views.ServiceTypeViewSet.as_view({'get': 'list'})),
    path('api/service/<int:pk>/', views.ServiceViewSet.as_view({'get': 'list'})),
    path('api/', include(router.urls)),
]

# =======================================================================================================

html_router = routers.DefaultRouter()
html_router.register('doctors', viewshtml.Doctors)
html_router.register('about', viewshtml.About, basename='about')
html_router.register('', viewshtml.Index)

urlpatterns += [
    path('service/', viewshtml.servicetype.as_view({'get': 'list'})),
    path('service/<int:pk>/', viewshtml.service.as_view({'get': 'list'})),
    path('appointment/', TemplateView.as_view(template_name='appointment.html')),
    path('contact/', TemplateView.as_view(template_name='contact.html')),
    path('', include(html_router.urls)),    
]