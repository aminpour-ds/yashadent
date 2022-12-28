from rest_framework.viewsets import ModelViewSet
from .serializers import DoctorSerializer
from .models import Doctor


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    