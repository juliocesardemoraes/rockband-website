from rest_framework import serializers
from bands import models

class BandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Band
        fields = '__all__'

