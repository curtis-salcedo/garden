from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile, Garden, Plant, Address, UserPlant
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "is_staff", "is_active")
    list_filter = ("username", "email","is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2", "is_staff", "is_manager",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

class GardenAdmin(admin.ModelAdmin):
    list = ("id", "profile", "name", "description", "size_x", "size_y")

class ProfileAdmin(admin.ModelAdmin):
    list = ("id", "user", "first_name", "last_name", "bio", "address", "user_plants")

class PlantAdmin(admin.ModelAdmin):
    list = ("id", "name", "type", "description", "sunlight", "water", "soil", "temperature", "humidity", "maturity", "size_x", "size_y")

class AddressAdmin(admin.ModelAdmin):
    list = ("id", "profile", "street", "city", "state", "zipcode")

class UserPlantAdmin(admin.ModelAdmin):
    list = ("id", "profile", "plant", "garden", "date_planted", "date_harvested", "is_alive")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Garden, GardenAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserPlant, UserPlantAdmin)



