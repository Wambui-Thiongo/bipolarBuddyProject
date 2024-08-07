from rest_framework import serializers
from .models import *
from django.db.models import Q
from accounts.models import Departments

class VitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vitals
        fields='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class TremorsSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(write_only=True)

    class Meta:
        model = Tremors
        fields = ['user_email',]

    def create(self, validated_data):
        user_email = validated_data.pop('user_email')
        try:
            patient = Patient.objects.get(Q(user__email=user_email) | Q(user__username=user_email))
        except Patient.DoesNotExist as e:
            print(e)
            raise serializers.ValidationError("Patient with this email does not exist.")

        tremor = Tremors.objects.create(patient=patient)
        return tremor
