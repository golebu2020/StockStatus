from django.shortcuts import render
from rest_framework import generics
from .models import Paint
from core.serializers import PaintSerializer



class PaintList(generics.ListCreateAPIView):
    """
    Implements listing and creating of the Paint List in the form of
    color | availability | inventory
    """
    queryset = Paint.objects.all()
    serializer_class = PaintSerializer


class PaintModify(generics.RetrieveUpdateAPIView):
    """
    Updates the Inventory
    """
    queryset = Paint.objects.all()
    serializer_class = PaintSerializer
