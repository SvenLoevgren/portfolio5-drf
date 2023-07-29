from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ApiEndpointTestCase(APITestCase):
    def setUp(self):
        # Create a test user and obtain a token for the user
        self.test_user = User.objects.create_user(username='svempatest', password='test666')
        self.token = Token.objects.create(user=self.test_user)

    def test_api_bookings_authenticated(self):
        # Test api/bookings endpoint with an authenticated user
        url = reverse('booking-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_menu_authenticated(self):
        # Test api/menu endpoint with an authenticated user
        url = reverse('menu-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_menu_unauthenticated(self):
        # Test api/menu endpoint without authentication
        url = reverse('menu-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
