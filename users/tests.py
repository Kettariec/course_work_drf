from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_register(self):
        data = {
            'email': 'test@test.org',
            'password': 'testpass',
            'telegram_id': '12345678'
        }

        response = self.client.post(
            reverse('users:register'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 6, 'email': 'test@test.org'}
        )
