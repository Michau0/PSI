from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Animal, Client, Adoption, Reservation, Playpen, HealthRecord
from .serializers import AnimalSerializer, ClientSerializer, ReservationSerializer, AdoptionSerializer, PlaypenSerializer, HealthRecordSerializer


class AnimalViewSet(viewsets.ViewSet):
    queryset = Animal.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        serializer = AnimalSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ClientViewSet(viewsets.ViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def list(self, request):
        serializer = ClientSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AdoptionViewSet(viewsets.ViewSet):
    queryset = Adoption.objects.all()
    def list(self, request):
        serializer = AdoptionSerializer(self.queryset, many=True)
        return Response(serializer.data)

class ReservationViewSet(viewsets.ViewSet):
    queryset = Reservation.objects.all()
    def list(self, request):
        serializer = ReservationSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PlaypenViewSet(viewsets.ViewSet):
    queryset = Playpen.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        serializer = PlaypenSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PlaypenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class HealthRecordViewSet(viewsets.ViewSet):
    queryset = HealthRecord.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        serializer = HealthRecordSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PlaypenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
