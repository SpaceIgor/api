from rest_framework import generics

from .models import CustomPerson, Team
from .serializers import CustomPersonSerializer, TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamList(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class CustomPersonList(generics.ListCreateAPIView):
    serializer_class = CustomPersonSerializer
    queryset = CustomPerson.objects.all()


class CustomPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomPersonSerializer
    queryset = CustomPerson.objects.all()

