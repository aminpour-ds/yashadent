from rest_framework import serializers
from .models import Doctor



class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['professionalStatement', 'mobile', 'first_name', 'last_name', 'email']
