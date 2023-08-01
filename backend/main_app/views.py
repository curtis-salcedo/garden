import json

# rest_framework imports
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# django imports
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Model imports
from .models import CustomUser, Profile, Garden, Plant, Address, UserPlant

# Serializer imports
from .serializers import CustomUserSerializer, ProfileSerializer, GardenSerializer, PlantSerializer, AddressSerializer, UserPlantSerializer, UserPlantDetailSerializer, UserPlantCreateSerializer

class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class GardenView(viewsets.ModelViewSet):
    serializer_class = GardenSerializer
    queryset = Garden.objects.all()

class PlantView(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class UserPlantView(viewsets.ModelViewSet):
    queryset = UserPlant.objects.all()
    serializer_class = UserPlantSerializer

    # def get_serializer_class(self):
    #     if self.action == 'list' or self.action == 'retrieve':
    #         return UserPlantDetailSerializer
    #     else:
    #         return UserPlantCreateSerializer
        
    # def get_queryset(self):
    #     pass
        # user = self.request.user
        # return UserPlant.objects.filter(user=user)

    # def create(self, request, *args, **kwargs):
    #     print('create user plant', request.data)
    #     data = request.data
    #     user = request.user
    #     plant = Plant.objects.get(id=data['plant'])
    #     user_plant = UserPlant.objects.create(user=user, plant=plant, date_planted=data['date_planted'], date_transplanted=data['date_transplanted'], date_harvested=data['date_harvested'])
    #     user_plant.save()
    #     return Response(UserPlantDetailSerializer(user_plant).data, status=status.HTTP_201_CREATED)
    
    # def update(self, request, *args, **kwargs):
    #     pass
        # print('update user plant', request.data)
        # data = request.data
        # user = request.user
        # plant = Plant.objects.get(id=data['plant'])
        # user_plant = UserPlant.objects.get(id=data['id'])
        # user_plant.user = user
        # user_plant.plant = plant
        # user_plant.date_planted = data['date_planted']
        # user_plant.date_transplanted = data['date_transplanted']
        # user_plant.date_harvested = data['date_harvested']
        # user_plant.save()
        # return Response(UserPlantDetailSerializer(user_plant).data, status=status.HTTP_201_CREATED)

    # def destroy(self, request, *args, **kwargs):
    #     pass
        # print('destroy user plant', request.data)
        # data = request.data
        # user_plant = UserPlant.objects.get(id=data['id'])
        # user_plant.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        # Compare this snippet from backend/main_app/urls.py:
        # Path: backend/main_app/urls.py
        # Compare this snippet from backend/main_app/views.py:
        # from rest_framework import viewsets

@api_view(['GET'])
def get_user(request):
    print("Check User Request data:", request)
    if request.user.is_authenticated:
        user_data = {
            'email': request.user.email,
            'name': request.user.name,
            'business': request.user.business.business_id,
        }
        print(user_data)
        return JsonResponse(user_data, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'User is not authenticated.'})