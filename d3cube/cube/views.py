from django.shortcuts import render
from rest_framework import generics
from . import models, serializers

# Create your views here.
def default(request):
    ct_filter = request.GET.get('filter', None)
    cube_type = request.GET.get('ct', None)
    in_cube = request.GET.get('in_cube', None)

    queryset = models.Cube.objects.all()
    if ct_filter:
        queryset = queryset.filter(character_type__short_name=ct_filter)

    if cube_type:
        queryset = queryset.filter(cube_slot__name=cube_type)

    if in_cube:
        print(in_cube)
        queryset = queryset.filter(in_cube=in_cube)

    return render(request, 'cube/default.html', {'items': queryset})


class Update(generics.UpdateAPIView):
    queryset = models.Cube.objects.all()
    serializer_class = serializers.CubeSerializer
