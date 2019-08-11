from rest_framework import serializers
from .models import adoption

class adoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = adoption
        fields = '__all__'