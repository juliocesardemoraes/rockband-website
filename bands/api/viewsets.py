from rest_framework import viewsets
from bands.api import serializers
from bands import models

class BandViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BandsSerializer
    queryset = models.Band.objects.all()