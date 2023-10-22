from rest_framework import serializers
from .models import CustomPerson, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')


class CustomPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPerson
        fields = ('__all__')