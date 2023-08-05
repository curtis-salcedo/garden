from rest_framework import serializers, permissions
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

# Model imports
from .models import CustomUser, Profile, Garden, Plant, Address, UserPlant

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    def create(self, validated_data):
        print('create custom user serializer', validated_data)
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)
        return super().create(validated_data)
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'bio', 'user_plants')

class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ('id', 'profile', 'name', 'description', 'size_x', 'size_y')

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name', 'type', 'season', 'description', 'image')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'profile', 'street', 'city', 'state', 'zipcode')

class UserPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlant
        fields = ('id', 'user', 'plant', 'date_planted', 'date_transplanted', 'date_harvested')

class UserPlantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlant
        fields = ('id', 'user', 'plant', 'date_planted', 'date_transplanted', 'date_harvested')

class UserPlantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlant
        fields = ('id', 'user', 'plant', 'date_planted', 'date_transplanted', 'date_harvested')