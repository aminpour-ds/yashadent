from rest_framework import serializers
from .models import Doctor, Service, Insurance, Review, About, DoctorImage, ServiceType, ServiceTypeImage, AppointmentRequest, Questions, ClinicVideo, ClinicImage



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
        fields = ['id', 'name', 'images', 'description', 'last_update']


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['servicetype', 'name', 'cost']


class InsuranceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Insurance
        fields = ['name']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['name', 'description', 'date']


class ClinicImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClinicImage
        fields = ['id', 'name', 'image']


class ClinicVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClinicVideo
        fields = ['id', 'name', 'video']

class AboutSerializer(serializers.ModelSerializer):
    images = ClinicImageSerializer(many=True, read_only=True)
    videos = ClinicVideoSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = ['description', 'email', 'linkedin', 'instagram', 'whatsapp', 'phone1', 'phone2', 'country', 'city', 'street', 'flat', 'images', 'videos']

        
class AppointmentRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppointmentRequest
        fields = ['name', 'your_problem', 'phone', 'description', 'date']

        
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ['id', 'question', 'description', 'date']
