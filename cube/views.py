from django.shortcuts import render
from rest_framework import generics
from . import models, serializers

# Create your views here.
def default(request):
    character_type = request.GET.get('characterType', None)
    cube_type = request.GET.get('cubeType', None)
    in_cube = request.GET.get('showCubedItems', None)

    queryset = models.Cube.objects.all()
    if character_type:
        character_type = int(character_type)
        queryset = queryset.filter(character_type__id=character_type)

    if cube_type:
        cube_type = int(cube_type)
        queryset = queryset.filter(cube_slot__id=cube_type)

    if in_cube:
        if in_cube == "True":
            in_cube = True
        else:
            in_cube = False

        queryset = queryset.filter(in_cube=in_cube)

    context = {
        'items': queryset,
        'character_type': character_type,
        'cube_type': cube_type,
        'in_cube': in_cube,
        'character_type_list': models.CharacterType.objects.all().order_by('name'),
        'cube_type_list': models.CubeType.objects.all().order_by('name'),
    }

    return render(request, 'cube/default.html', context)


class Update(generics.UpdateAPIView):
    queryset = models.Cube.objects.all()
    serializer_class = serializers.CubeSerializer
