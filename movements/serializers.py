from datetime import time

import ipdb
from rest_framework import serializers

from movements_store.models import MovementStore
from movements_store.serializers import MovementStoreSerializer
from owners.models import Owner
from stores.models import Store
from utils import choice

from .models import Movement


class MovementSerializer(serializers.ModelSerializer):

    movement_list = MovementStoreSerializer(read_only=True, many=True)

    class Meta:
        model = Movement
        fields = '__all__'
        read_only_fields = ['id', 'registered_at']

    def create(self, validated_data):
        document = Movement.objects.create(**validated_data)

        with open(f'./files-cnab/{str(document.document)}') as file_data:
            file = file_data.readlines()

            for line in file:

                time_currence = str(time(hour=int(line[42:44]), minute=int(line[44:46]), second=int(line[46:48])))
                date_currence = f'{line[1:5]}/{line[5:7]}/{line[7:9]}'

                transaction_type=choice(line[0])
                transaction_value=str(float(line[9:19])/100.00)
                cpf=line[19:30]
                card=line[30:42]
                owner=line[48:62].strip()
                store_name=line[62:80].strip()


                owner_object = Owner.objects.get_or_create(name=owner, cpf=cpf)
                store_object = Store.objects.get_or_create(name=store_name, owner=owner_object[0])

                MovementStore.objects.create(
                    transaction_type=transaction_type,
                    date_of_currence=date_currence,
                    transaction_value=transaction_value,
                    card=card,
                    time=time_currence,
                    store=store_object[0],
                    doc_cnab=document
                )
    
        return document