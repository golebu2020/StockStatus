from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import CustomUser
from core.serializers import CustomUserPermissionSerializer


# Create your views here.
class CustomUserUpdatePermission(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserPermissionSerializer
    permmission_classes = [IsAdminUser]


class CustomUserListPermission(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserPermissionSerializer
    permmission_classes = [IsAdminUser]

