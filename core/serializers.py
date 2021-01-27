from rest_framework import serializers

from core.models import Bunny, BreedingFarm


class BreedingFarmSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        allow_null=True,
        required=False,
    )
    name = serializers.CharField(
        max_length=255,
    )
    city = serializers.CharField(
        max_length=255,
    )

    def create(self, validated_data):
        return BreedingFarm(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)


class BunnySerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=255,
    )
    age = serializers.FloatField()
    furr_color = serializers.CharField(
        max_length=255,
    )
    breeding_farm_id = serializers.IntegerField()

    def create(self, validated_data):
        return Bunny(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.furr_color = validated_data.get('furr_color', instance.furr_color)
        instance.breeding_farm_id = validated_data.get('breeding_farm_id', instance.breeding_farm_id)
        instance.save()
        return instance
