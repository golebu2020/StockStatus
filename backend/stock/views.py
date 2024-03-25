from django.shortcuts import render
from rest_framework import generics
from .models import Paint
from core.serializers import PaintSerializer


class PaintList(generics.ListCreateAPIView):
    queryset = Paint.objects.all()
    serializer = PaintSerializer
    pass
