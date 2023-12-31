from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db.models.signals import post_save

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, null=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=128, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zipcode = models.IntegerField(blank=True)

    def __str__(self):
        return self.street + ', ' + self.city + ', ' + self.state
    
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    bio = models.TextField(max_length=500, blank=True)
    # garden = models.ForeignKey('Garden', on_delete=models.CASCADE, null=True, blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    user_plants = models.ManyToManyField('Plant', blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.email



class Plant(models.Model):
    TYPE_CHOICES = [
        ('vegetable', 'Vegetable'),
        ('fruit', 'Fruit'),
        ('herb', 'Herb'),
        ('flower', 'Flower'),
        ('other', 'Other'),
    ]
    SEASON_CHOICES = [
        ('cool', 'Cool'),
        ('warm', 'Warm'),
        ('any', 'Any'),
    ]
    SUN_CHOICES = [
        ('full', 'Full'),
        ('partial', 'Partial'),
        ('shade', 'Shade'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    color = models.CharField(max_length=100, blank=True)
    # image = models.ImageField(upload_to='plant_pics', blank=True, null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='vegetable')
    season = models.CharField(max_length=100, choices=SEASON_CHOICES, default='any')
    sun = models.CharField(max_length=100, choices=SUN_CHOICES, default='full')
    temp_min = models.IntegerField(blank=True, null=True)
    temp_ideal = models.IntegerField(blank=True, null=True)
    temp_max = models.IntegerField(blank=True, null=True)
    spacing_x_min = models.IntegerField(blank=True, null=True)
    spacing_x_max = models.IntegerField(blank=True, null=True)
    spacing_y_min = models.IntegerField(blank=True, null=True)
    spacing_y_max = models.IntegerField(blank=True, null=True)
    height_min = models.IntegerField(blank=True, null=True)
    height_max = models.IntegerField(blank=True, null=True)
    width_min = models.IntegerField(blank=True, null=True)
    width_max = models.IntegerField(blank=True, null=True)
    depth_min = models.IntegerField(blank=True, null=True)
    depth_max = models.IntegerField(blank=True, null=True)
    germination_min = models.IntegerField(blank=True, null=True)
    germination_max = models.IntegerField(blank=True, null=True)
    harvest_min = models.IntegerField(blank=True, null=True)
    harvest_max = models.IntegerField(blank=True, null=True)
    days_to_transplant_min = models.IntegerField(blank=True, null=True)
    days_to_transplant_max = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.description
    
class UserPlant(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True, blank=True)
    garden = models.ForeignKey('Garden', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    notes = models.TextField(max_length=500, blank=True)
    # image = models.ImageField(upload_to='user_plant_pics', blank=True, null=True)
    date_planted = models.DateField(blank=True, null=True)
    date_transplanted = models.DateField(blank=True, null=True)
    date_harvested = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.garden.name + ' - ' + self.user.profile.user.email

class Garden(models.Model):
    FACE_CHOICES = [
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ]
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    size_x = models.IntegerField(blank=True, null=True)
    size_y = models.IntegerField(blank=True, null=True)
    direction = models.CharField(max_length=100, choices=FACE_CHOICES, default='north')

    def __str__(self):
        return self.name
    
    def get_profile(self):
        if self.profile is None:
            current_user = CustomUser.objects.get(id=self.user.id)

            self.profile = Profile.objects.get(user=current_user)
            self.save()
        return self.profile
