from rest_framework.viewsets import ModelViewSet
from .serializers import DoctorSerializer, ServiceSerializer, InsuranceSerializer, ReviewSerializer
from .models import Doctor, Service, Insurance, Review
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


class InsuranceViewSet(ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [IsAdminOrReadOnly]

    
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrReadOnly]
    