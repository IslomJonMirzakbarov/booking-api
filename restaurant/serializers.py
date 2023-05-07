from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Booking, Menu


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
