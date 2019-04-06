from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class MyProfile(APIView):
    pass

class ToysCreate():
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