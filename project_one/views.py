# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from project_one.serializers import UserSerializer, GroupSerializer, StateSerializer, CitySerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from project_one.models import State, City
from rest_framework import generics, status, serializers, viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
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

@api_view(['GET'])
def state_list(request):
    states = State.objects.all()
    serializer = StateSerializer(states, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def state_add(request):
    serializer = StateSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def state_edit(request, id):
    state = State.objects.get(id=id)
    serializer = StateSerializer(state, data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST']) 
def state_del(request, id):
    state = State.objects.get(id=id)
    state.delete()
    return HttpResponse(status=204)

@api_view(['GET'])
def city_list(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def city_add(request):
    #state = State.objects.get(id=state_id)
    serializer = CitySerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def city_edit(request, id):
    city = City.objects.get(id=state_id)
    serializer = CitySerializer(city, data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST']) 
def city_del(request, id):
    city = City.objects.get(id=id)
    city.delete()
    return HttpResponse(status=204)

def index(request):
    return render(request, 'index.html', {})