from django.shortcuts import render
from rest_framework import generics, status
from .serializers import AnnualSerializer
from .models import Annual
from rest_framework.views import APIView
from rest_framework.response import Response

class AnnualView(generics.ListAPIView):
    queryset = Annual.objects.all()
    serializer_class = AnnualSerializer
