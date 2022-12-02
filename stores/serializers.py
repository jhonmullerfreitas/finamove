from rest_framework import serializers
from .models import Store
import ipdb

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'
        