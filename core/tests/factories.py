from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from core.models import Bunny, BreedingFarm


class BreedingFarmFactory(DjangoModelFactory):
    name = Faker('name')
    city = Faker('name')

    class Meta:
        model = BreedingFarm


class BunnyFactory(DjangoModelFactory):
    name = Faker('name')
    age = '2'
    furr_color: 'green'
    breeding_farm = SubFactory(BreedingFarmFactory)

    class Meta:
        model = Bunny
