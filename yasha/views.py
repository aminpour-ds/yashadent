from rest_framework.viewsets import ModelViewSet
from .serializers import DoctorSerializer, ServiceSerializer, InsuranceSerializer, ReviewSerializer, AboutSerializer, ServiceTypeSerializer, AppointmentRequestSerializer, QuestionSerializer
from .models import Doctor, Service, Insurance, Review, About, ServiceType, AppointmentRequest, Questions
from .permissions import IsAdminOrReadOnly, IsAdminOrPatient
from .pagination import DefaultPagination


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination


class ServiceViewSet(ModelViewSet):    
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Service.objects.filter(servicetype_id=self.kwargs['pk'])

    def get_serializer_context(self):
        return {'servicetype_id': self.kwargs['pk']}


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


class AppointmentRequestViewSet(ModelViewSet):        
    http_method_names = ['get', 'post', 'head', 'options']    
    queryset = AppointmentRequest.objects.all()
    serializer_class = AppointmentRequestSerializer


class QuestionsViewSet(ModelViewSet):         
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrPatient]
    
           
