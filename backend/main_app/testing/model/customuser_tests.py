#import test case
from django.test import TestCase

from main_app.models import CustomUser

class CustomUserTest(TestCase):

    def test_create_user(self):
        user = CustomUser.objects.create(
            username='testuser',
            email='test@test.com',
            first_name='Test',
            last_name='User',
            is_staff=False,
            is_active=True,
            )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@test.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_active, True)