from django.test import TestCase

from main_app.models import Profile, CustomUser

class ProfileTest(TestCase):

    # Create a profile from the custom user
    def test_create_profile(self):
        user = CustomUser.objects.create(
            username='testuser',
            email='test@test.com',
            first_name='Test',
            last_name='User',
            is_staff=False,
            is_active=True,
            )
        profile = Profile.objects.create(
            user=user,
            bio='This is a test bio',
            address='123 Test St',
            )
        self.assertEqual(profile.user, user)
        self.assertEqual(profile.bio, 'This is a test bio')
        self.assertEqual(profile.address, '123 Test St')
        self.assertEqual(profile.user_plants.count(), 0)
        self.assertEqual(profile.addresses.count(), 0)

    