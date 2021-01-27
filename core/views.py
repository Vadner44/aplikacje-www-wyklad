from django.http import HttpResponse

# Create your views here.
from rest_framework import authentication, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Bunny, BreedingFarm
from core.paginations import CustomPagination
from core.serializers import BunnySerializer, BreedingFarmSerializer


def check_if_none(dict, key, value):
    if value:
        dict[key] = value


class BunnyView(GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = Bunny
    serializer_class = BunnySerializer
    pagination_class = CustomPagination

    def get(self, request, format=None):
        name = request.GET.get('name', None)
        age = request.GET.get('age', None)
        filter_dict = {}
        check_if_none(filter_dict, 'age', age)
        check_if_none(filter_dict, 'name', name)
        bunnies = [self.serializer_class(bunny).data for bunny in self.queryset.objects.filter(**filter_dict)]
        return Response(bunnies)


class CreateBunnyView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        new_bunny = BunnySerializer(data=request.data)
        new_bunny.is_valid()
        print(new_bunny.errors)
        if new_bunny.errors:
            return HttpResponse(new_bunny.errors)
        new_bunny.save().save()
        return HttpResponse(f'Object {new_bunny.instance.name} created')


class UpdateBunnyView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        bunny = Bunny.objects.get(id=request.data['id'])
        bunny_serializer = BunnySerializer(bunny, data=request.data['update'])
        bunny_serializer.is_valid()
        if bunny_serializer.errors:
            return HttpResponse(bunny_serializer.errors)
        bunny_serializer.update(bunny, bunny_serializer.validated_data).save()
        return HttpResponse(f'Object {bunny.name} update')


class BreedingFarmView(GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = BreedingFarm
    serializer_class = BreedingFarmSerializer
    pagination_class = CustomPagination

    def get(self, request, format=None):
        name = request.GET.get('name', None)
        city = request.GET.get('city', None)
        order_by = request.GET.get('order_by', 'id')
        order_by_dict = {}
        filter_dict = {}
        check_if_none(filter_dict, 'age', city)
        check_if_none(filter_dict, 'name', name)

        breeding_farms = [self.serializer_class(breeding_farm).data for breeding_farm in self.queryset.objects.filter(**filter_dict).order_by(order_by)]
        return Response(breeding_farms)


class CreateBreedingFarmView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        new_breeding_farm = BreedingFarmSerializer(data=request.data)
        new_breeding_farm.is_valid()
        print(new_breeding_farm.errors)
        if new_breeding_farm.errors:
            return HttpResponse(new_breeding_farm.errors)
        new_breeding_farm.save().save()
        return HttpResponse(f'Object {new_breeding_farm.instance.name} created')


class UpdateBreedingFarmView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        breeding_farm = BreedingFarm.objects.get(id=request.data['id'])
        breeding_farm_seializer = BreedingFarmSerializer(breeding_farm, data=request.data['update'])
        breeding_farm_seializer.is_valid()
        if breeding_farm_seializer.errors:
            return HttpResponse(breeding_farm_seializer.errors)
        breeding_farm_seializer.update(breeding_farm, breeding_farm_seializer.validated_data).save()
        return HttpResponse(f'Object {breeding_farm.name} update')
