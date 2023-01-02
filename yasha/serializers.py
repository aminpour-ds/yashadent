from rest_framework import serializers
from .models import Doctor, Service, Insurance, Review, About, DoctorImage, ServiceType, ServiceTypeImage, AppointmentRequest



class DoctorImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        doctor_id = self.context['doctor_id']
        return DoctorImage.objects.create(doctor_id=doctor_id, **validated_data)

    class Meta:
        model = DoctorImage
        fields = ['id', 'image']


class DoctorSerializer(serializers.ModelSerializer):
    images = DoctorImageSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ['professionalStatement', 'mobile', 'first_name', 'last_name', 'email', 'images']


class ServiceTypeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTypeImage
        fields = ['id', 'image']


class ServiceTypeSerializer(serializers.ModelSerializer):
    images = ServiceTypeImageSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceType
        fields = ['id', 'name', 'images']


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['ServiceTypeID', 'name', 'cost']


class InsuranceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Insurance
        fields = ['name']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['name', 'description', 'date']


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ['description', 'email', 'linkedin', 'instagram', 'whatsapp', 'phone1', 'phone2', 'address']

        
class AppointmentRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppointmentRequest
        fields = ['name', 'your_problem', 'phone', 'description', 'date']
