from rest_framework import serializers
from .models import Doctor, Service, Insurance, Review



class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['professionalStatement', 'mobile', 'first_name', 'last_name', 'email']


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
