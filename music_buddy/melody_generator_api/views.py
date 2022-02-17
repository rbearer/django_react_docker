from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Create your views here.
def main(request):
  return HttpResponse("Hello")

class UserNew(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserIndex(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
