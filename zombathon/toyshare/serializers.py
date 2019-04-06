from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ExtUserSerializer(serializers.ModelSerializer):
    login = serializers.SerializerMethodField()

    class Meta:
        model = ExtUser

        fields = ('userbase', 'tel',
                  'city', 'street', 'house_number',
                  'post_code', 'age', 'login', 'rank')

    def get_login(self, object):
        return object.login


class ToySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Toy
        fields = ('id', 'name', 'description',
                  'photo_path',
                  'condition', 'age',
                  'players_quantity', 'owner')


class RentingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renting
        fields = ('begin_date', 'toy_id_ref',
                  'owner_id_ref', 'user_id_ref')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renting
        fields = ('value', 'message', 'toy_condition',
                  'renting_id_ref', 'user_id_ref')


class WantedSerializer(serializers.ModelSerializer):
    user_id_ref = serializers.ReadOnlyField(source='user_id_ref.id')
    class Meta:
        model = Wanted
        fields = ('toy_id_ref', 'user_id_ref')

class UnwantedSerializer(serializers.ModelSerializer):
    user_id_ref = serializers.ReadOnlyField(source='user_id_ref.id')
    class Meta:
        model = Unwanted
        fields = ('toy_id_ref','user_id_ref')