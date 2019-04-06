from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from toyshare.serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


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
    queryset = Toy.objects.all()
    serializer_class = ToySerializer


class RentingList(generics.ListAPIView):
    queryset = Renting.objects.all()
    serializer_class = RentingSerializer


class RentingDetail(generics.RetrieveDestroyAPIView):
    queryset = Renting.objects.all()
    serializer_class = RentingSerializer
