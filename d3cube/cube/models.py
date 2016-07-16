from django.db import models

# Create your models here.
class Cube(models.Model):
    CHARACTER_TYPE_CHOICES = (
        ('All', 'All',),
        ('Barbarian', 'Barbarian',),
        ('Crusader', 'Crusader',),
        ('Demon Hunter', 'Demon Hunter',),
        ('Monk', 'Monk',),
        ('Witch Doctor', 'Witch Doctor',),
        ('Wizard', 'Wizard',),
    )
    CUBE_SLOT_CHOICES = (
        ('Weapon', 'Weapon',),
        ('Armor', 'Armor',),
        ('Jewelry', 'Jewelry',),
    )
    name = models.CharField(max_length=500)
    affix = models.TextField(blank=True, null=True)
    character_type = models.CharField(max_length=50, choices=CHARACTER_TYPE_CHOICES)
    cube_slot = models.CharField(max_length=50, choices=CUBE_SLOT_CHOICES)
    in_cube = models.BooleanField(default=False)
    in_stash = models.BooleanField(default=False)

    def __str__(self):
        return "{}: {}, {}".format(self.name, self.character_type, self.cube_slot)
