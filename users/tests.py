from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('register_user'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'SuperSafePassword123',
            'password2': 'SuperSafePassword123',
            'role': 'empleado',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())
