from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import Animal, Client, Adoption, Reservation, Playpen, LoyalityProgram, HealthRecord
from .serializers import AnimalSerializer, ClientSerializer, ReservationSerializer, AdoptionSerializer, PlaypenSerializer, LoyalityProgramSerializer, HealthRecordSerializer


class AnimalViewSet(viewsets.ViewSet):
    queryset = Animal.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def list(self, request):
        serializer = AnimalSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, request):



class ClientViewSet(viewsets.ViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def list(self, request):
        serializer = ClientSerializer(self.queryset, many=True)
        return Response(serializer.data)

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

class PlaypenViewSet(viewsets.ViewSet):
    queryset = Playpen.objects.all()
    def list(self, request):
        serializer = PlaypenSerializer(self.queryset, many=True)
        return Response(serializer.data)

class LoyaltyProgramViewSet(viewsets.ViewSet):
    queryset = LoyalityProgram.objects.all()
    def list(self, request):
        serializer = LoyalityProgramSerializer(self.queryset, many=True)
        return Response(serializer.data)

class HealthRecordViewSet(viewsets.ViewSet):
    queryset = HealthRecord.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def list(self, request):
        serializer = HealthRecordSerializer(self.queryset, many=True)
        return Response(serializer.data)
