from rest_framework import serializers
from . import models


class CubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cube
        fields = ('id', 'in_cube', 'in_stash',)
