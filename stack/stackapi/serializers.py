from rest_framework import serializers
from .models import Questions

class questionserializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('__all__')
