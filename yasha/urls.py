from django.urls import path, include
from rest_framework_nested import routers
from . import views, viewshtml


router = routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet)
router.register('services', views.ServiceViewSet)
router.register('insurance', views.InsuranceViewSet)
router.register('review', views.ReviewViewSet)
router.register('about', views.AboutViewSet, basename='about')

urlpatterns = [
    path('api/', include(router.urls)),
]

# =======================================================================================================

html_router = routers.DefaultRouter()
html_router.register('doctors', viewshtml.Doctors)
html_router.register('about', viewshtml.About, basename='about')
html_router.register('', viewshtml.Index)

urlpatterns += [
    path('', include(html_router.urls)),    
]