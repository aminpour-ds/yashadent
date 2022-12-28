from django.urls import path, include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet)
router.register('services', views.ServiceViewSet)
router.register('insurance', views.InsuranceViewSet)
router.register('review', views.ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]