from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ExtUserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    user_mail = serializers.EmailField()
    rank = serializers.IntegerField()

    class Meta:
        model = ExtUser
        fields = ('username', 'user_mail', 'tel',
                  'city', 'street', 'house_nunmber',
                  'post_code', 'age', 'login', 'rank')


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy


class RentingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renting


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renting


class WantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wants


class UnwantedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unwanted
