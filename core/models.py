from django.db import models

# Create your models here.


class BreedingFarm(models.Model):

    name = models.CharField(
        'Name',
        max_length=255,
    )
    city = models.CharField(
        'City',
        max_length=255,
    )


class Bunny(models.Model):
    name = models.CharField(
        'Name',
        max_length=255,
    )
    age = models.FloatField(
        'Age',
    )
    furr_color = models.CharField(
        'Furr color',
        max_length=255,
    )
    breeding_farm = models.ForeignKey(
        BreedingFarm,
        verbose_name='Breeding farm',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Bunny'
        verbose_name_plural = 'Bunnies'
