from rest_framework import serializers
from .models import Owner
import ipdb


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'

