from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from restaurant.models import Menu


class MenuViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='test@123!')
        self.client.login(username='testuser', password='test@123!')
        self.item1 = Menu.objects.create(title='IceCream', price=80)
        self.item2 = Menu.objects.create(title='Pizza', price=100)
        self.url = reverse('menuitems-list')

    def test_getall(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
