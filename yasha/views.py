from rest_framework.viewsets import ModelViewSet
from .serializers import DoctorSerializer, ServiceSerializer
from .models import Doctor, Service
from .permissions import IsAdminOrReadOnly


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminOrReadOnly]


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]
    