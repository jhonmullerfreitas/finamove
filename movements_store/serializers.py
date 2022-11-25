from rest_framework import serializers
from .models import MovementStore
import ipdb

class MovementStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovementStore
        fields = '__all__'