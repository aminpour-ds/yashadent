from rest_framework.viewsets import ModelViewSet
from .serializers import DoctorSerializer
from .models import Doctor
from .permissions import IsAdminOrReadOnly


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminOrReadOnly]
    