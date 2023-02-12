from django.urls import path, include
from rest_framework_nested import routers
from django.views.generic import TemplateView
from . import views, viewshtml


router = routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet)
router.register('colleague', views.ColleagueViewSet)
router.register('partners', views.PartnersViewSet)
router.register('about', views.AboutViewSet, basename='about')
router.register('samples', views.SamplesViewSet, basename='samples')
router.register('AppointmentRequest', views.AppointmentRequestViewSet)

urlpatterns = [
    path('api/service/', views.ServiceTypeViewSet.as_view({'get': 'list'})),
    path('api/service/<int:pk>/', views.ServiceViewSet.as_view({'get': 'list'})),
    path('api/', include(router.urls)),
]

# english=======================================================================================================

html_en_router = routers.DefaultRouter()
html_en_router.register('doctors', viewshtml.Doctors_EN)
html_en_router.register('partners', viewshtml.Partners_EN)
html_en_router.register('about', viewshtml.About_EN, basename='about')
html_en_router.register('samples', viewshtml.Samples_EN, basename='samples')
html_en_router.register('', viewshtml.Index_EN)

urlpatterns += [
    path('en/service/<int:pk>/', viewshtml.Servicetype_EN),
    path('en/appointment/', TemplateView.as_view(template_name='yasha-en/appointment.html')),    
    path('en/', include(html_en_router.urls)),    
]

# farsi=======================================================================================================

html_router = routers.DefaultRouter()
html_router.register('doctors', viewshtml.Doctors)
html_router.register('partners', viewshtml.Partners)
html_router.register('about', viewshtml.About, basename='about')
html_router.register('samples', viewshtml.Samples, basename='samples')
html_router.register('', viewshtml.Index)

urlpatterns += [
    path('service/<int:pk>/', viewshtml.Servicetype),
    path('appointment/', TemplateView.as_view(template_name='appointment.html')),
    path('', include(html_router.urls)),    
]