from rest_framework import serializers
from .models import Doctor, Service, Insurance, About, DoctorImage, ServiceType, ServiceTypeImage, \
AppointmentRequest, ClinicVideo, ClinicImage, DoctorPortfolio, ColleagueImage, Colleague



class ColleagueImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColleagueImage
        fields = ['id', 'image']


class ColleagueSerializer(serializers.ModelSerializer):
    images = ColleagueImageSerializer(many=True, read_only=True)

    class Meta:
        model = Colleague
        fields = ['first_name_fa', 'last_name_fa', 'professionalStatement_fa', 'first_name_en', 'last_name_en', 'professionalStatement_en', 'images']


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
        fields = ['first_name_fa', 'last_name_fa', 'professionalStatement_fa', 'mobile', 'email', 'images', 'first_name_en', 'last_name_en', 'professionalStatement_en']


class ServiceTypeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTypeImage
        fields = ['id', 'image']


class ServiceTypeSerializer(serializers.ModelSerializer):
    images = ServiceTypeImageSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceType
        fields = ['id', 'name_fa', 'images', 'description_fa', 'last_update', 'name_en', 'description_en']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['servicetype', 'name', 'cost']


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['name_fa', 'description_fa', 'name_en', 'description_en']


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
        fields = ['description_fa', 'email', 'linkedin', 'instagram', 'whatsapp', 'phone1', 'phone2', 'country_fa', 'city_fa', 'street_fa', 'flat_fa', 'workingـhours_fa', 'description_en', 'country_en', 'city_en', 'street_en', 'flat_en', 'workingـhours_en', 'images', 'videos']

        
class AppointmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentRequest
        fields = ['name', 'your_problem', 'phone', 'description', 'date']

        
class DoctorPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorPortfolio
        fields = ['id', 'doctor', 'title_fa', 'title_en', 'image_before', 'image_after']



# ===================================inactive ===========================================================

# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['name', 'description', 'date']


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name_fa', 'name_en']


# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Questions
#         fields = ['id', 'question_fa', 'description_fa', 'question_en', 'description_en', 'date']

