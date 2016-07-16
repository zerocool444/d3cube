from django.shortcuts import render
from rest_framework import generics
from . import models, serializers

# Create your views here.
def default(request):
    return render(request, 'cube/default.html', {'items': models.Cube.objects.all()})


class Update(generics.UpdateAPIView):
    queryset = models.Cube.objects.all()
    serializer_class = serializers.CubeSerializer
