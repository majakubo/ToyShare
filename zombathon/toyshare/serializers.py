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


class ExtUserSerializer(serializers.ModelSerializer):
    login = serializers.SerializerMethodField()

    class Meta:
        model = ExtUser
        fields = ('userbase', 'tel',
                  'city', 'street', 'house_number',
                  'post_code', 'age', 'login', 'rank', 'login',)

    def get_login(self, object):
        return object.login


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('name', 'description',
                  'photo_path',
                  'condition', 'age',
                  'players_quantity', 'user_id_ref')


class RentingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renting
        fields = ('begin_date', 'toy_id',
                  'owner_id', 'user_id_ref')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renting
        fields = ('value', 'message', 'toy_condition',
                  'renting_id_ref', 'user_id_ref')
