from rest_framework import viewsets

from world import models
from world import serializers


class InvasivePlantViewSet(viewsets.ModelViewSet):
    queryset = models.InvasivePlant.objects.all()
    serializer_class = serializers.InvasivePlantSerializer
