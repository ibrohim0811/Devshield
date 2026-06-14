from django.shortcuts import render
from rest_framework.generics import ( CreateAPIView, ListAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response


