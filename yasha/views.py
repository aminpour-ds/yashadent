from rest_framework.viewsets import ModelViewSet
from .serializers import DoctorSerializer, ServiceSerializer, InsuranceSerializer, ReviewSerializer, AboutSerializer, ServiceTypeSerializer
from .models import Doctor, Service, Insurance, Review, About, ServiceType
from .permissions import IsAdminOrReadOnly
from .pagination import DefaultPagination


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination


class ServiceTypeViewSet(ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination


class InsuranceViewSet(ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [IsAdminOrReadOnly]

    
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrReadOnly]
    

class AboutViewSet(ModelViewSet):            
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination
