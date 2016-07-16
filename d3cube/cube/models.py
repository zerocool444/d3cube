from django.db import models

# Create your models here.
class CubeType(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class CharacterType(models.Model):
    name = models.CharField(max_length=1000)
    short_name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Cube(models.Model):
    name = models.CharField(max_length=500)
    affix = models.TextField(blank=True, null=True)
    character_type = models.ManyToManyField(CharacterType, blank=True)
    cube_slot = models.ForeignKey(CubeType, blank=True, null=True)
    in_cube = models.BooleanField(default=False)
    in_stash = models.BooleanField(default=False)

    def __str__(self):
        return self.name
