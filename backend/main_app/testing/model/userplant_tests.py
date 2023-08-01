from django.test import TestCase

from main_app.models import UserPlant, Plant, Profile, CustomUser

class UserPlantTest(TestCase):
      
      def test_create_userplant(self):
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
          plant = Plant.objects.create(
              name='Test Plant',
              type='vegetable',
              season='any',
              )
          userplant = UserPlant.objects.create(
              user=profile,
              plant=plant,
              )
          self.assertEqual(userplant.user, profile)
          self.assertEqual(userplant.plant, plant)
          self.assertEqual(userplant.date_planted, None)
          self.assertEqual(userplant.date_transplanted, None)
          self.assertEqual(userplant.date_harvested, None)