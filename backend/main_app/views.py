import json

# rest_framework imports
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# django imports
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect

# Model imports
from .models import CustomUser, Profile, Garden, Plant, Address, UserPlant

# Serializer imports
from .serializers import CustomUserSerializer, ProfileSerializer, GardenSerializer, PlantSerializer, AddressSerializer, UserPlantSerializer, UserPlantDetailSerializer, UserPlantCreateSerializer

class CustomUserView(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class GardenView(viewsets.ModelViewSet):
    serializer_class = GardenSerializer
    queryset = Garden.objects.all()

class PlantView(viewsets.ModelViewSet):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class UserPlantView(viewsets.ModelViewSet):
    serializer_class = UserPlantSerializer
    queryset = UserPlant.objects.all()

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
def home(request):
    return render(request, 'home.html')

def proxy_login(request):
    print('Proxy Login request:', request)
    redirect_url = 'http://localhost:8000/accounts/login/'
    login_success = True
    if login_success:
        close_script = '''
        <script>
            window.opener.postMessage('login_success', '*');
            window.close();
        </script>
        '''
        return JsonResponse({'redirect_url': redirect_url, 'login_success': True, 'close_script': close_script}, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse({'redirect_url': redirect_url, 'login_success': False}, status=status.HTTP_200_OK, safe=False)
    
def proxy_signup(request):
    print('Sign Up Proxy request:', request)
    redirect_url = 'http://localhost:8000/accounts/login/'
    return JsonResponse({'redirect_url': redirect_url}, status=status.HTTP_200_OK, safe=False)

def proxy_logout(request):
    print('Proxy Logout request:', request)
    redirect_url = 'http://localhost:8000/accounts/logout/'
    return JsonResponse({'redirect_url': redirect_url}, status=status.HTTP_200_OK, safe=False)

def redirect_view(request):
    print("Redirect request:", request)
    redirect_url = 'http://localhost:3000/'
    return HttpResponseRedirect(redirect_url)
    
@api_view(['GET'])
def get_user(request):
    print("Check User Request data:", request)
    print("user authenticated:", request.user)
    if request.user.is_authenticated:
        user_data = {
            'email': request.user.email,
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        print(user_data)
        return JsonResponse(user_data, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'User is not authenticated.'})