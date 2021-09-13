
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
class profileAPI(viewsets.ModelViewSet):
    serializer_class = profileSerializer
    queryset = profile.objects.all()[:5]