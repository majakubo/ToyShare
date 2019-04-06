from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from toyshare.serializers import *
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MyProfile(APIView):
    pass


class ToysCreate(APIView):
    pass


class ToysList(generics.ListAPIView):
    pass


class ToysDetail(generics.RetrieveUpdateDestroyAPIView):
    pass


class SearchList(generics.ListAPIView):
    pass


class RentingList(generics.ListAPIView):
    pass


class RentingDetail(generics.RetrieveDestroyAPIView):
    pass
