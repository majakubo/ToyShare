from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from toyshare.serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from .permissions import IsOwnerOrReadOnly
import toyshare.distance as d


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MyProfile(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ExtUser.objects.all()
    serializer_class = ExtUserSerializer


class ToysList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Toy.objects.all()
    serializer_class = ToySerializer


class ToysDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Toy.objects.all()
    serializer_class = ToySerializer


class ToySearchList(generics.ListAPIView):
    '''
    def get_queryset(self):
        user = User.objects.get(id=self.request.user.id)
        ext_user = list(ExtUser.objects.get(userbase=user))
        #toy
        owner = list((Wants.objects.get(toy_id_ref=toy.id)).user_id_ref)

        loc_user = ext_user[0].street + ext_user[0].house_number +ext_user[0].city
        loc_owner = owner[0].street +owner[0].house_number +owner[0].city

        dist = d.calculate_distance(loc_user, loc_owner)
        print(dist)
    '''

    queryset = Renting.objects.all()
    serializer_class = ToySerializer





class RentingList(generics.ListAPIView):
    #queryset = Renting.objects.all()
    serializer_class = RentingSerializer

    def get_queryset(self):
        user = User.objects.get(id=self.request.user.id)
        ext_user = ExtUser.objects.get(userbase=user)

        a = Renting.objects.filter(owner_id_ref=ext_user.id)
        b = Renting.objects.filter(user_id_ref=ext_user.id)
        return a.union(b)



class RentingDetail(generics.RetrieveDestroyAPIView):
    #queryset = Renting.objects.all()
    serializer_class = RentingSerializer
    def get_queryset(self):
        user = User.objects.get(id=self.request.user.id)
        ext_user = ExtUser.objects.get(userbase=user)
        print(ext_user)

        a = Renting.objects.filter(owner_id_ref=ext_user.id)
        b = Renting.objects.filter(user_id_ref=ext_user.id)

        return a.union(b)


class WantedList(generics.ListCreateAPIView):
    queryset = Wanted.objects.all()
    serializer_class = WantedSerializer

class UnwantedList(generics.ListCreateAPIView):
    queryset = Unwanted.objects.all()
    serializer_class = UnwantedSerializer


