"""
URL configuration for garden project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main_app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Router registration
router = routers.DefaultRouter()
router.register('users', views.CustomUserView)
router.register('plants', views.PlantView)
router.register('gardens', views.GardenView)


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),

    # JWT URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # Authentication URLs
    path('proxy/accounts/login/', views.proxy_login, name='proxy_login'),
    path('proxy/accounts/logout/', views.proxy_logout, name='proxy_logout'),
    path('proxy/accounts/signup/', views.proxy_signup, name='proxy_signup'),
    path('redirect/', views.redirect_view, name='redirect'),
    path('api/user/get', views.get_user, name='get_user'),

    # Plant URLs
    # Garden URLs
    # Profile URLs
    # Address URLs
    # UserPlant URLs

]
