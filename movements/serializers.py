import ipdb
from rest_framework import serializers
from datetime import time
from owners.models import Owner
from stores.models import Store
from movements_store.models import MovementStore

from .models import Movement


class MovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movement
        fields = '__all__'
        read_only_fields = ['id', 'registered_at']


    def create(self, validated_data):

        document = Movement.objects.create(**validated_data)

        name_file = str(document.document)

        movements_data = []
        with open(f'./files-cnab/{name_file}') as file_data:
            file = file_data.readlines()

            for line in file:
                line_data = line
                time_currence = time(hour=int(line_data[42:44]), minute=int(line_data[44:46]), second=int(line_data[46:48]))
                transaction_data = {
                    "transaction_type" : line_data[0],
                    "date_of_currence" : line_data[1:9],
                    "transaction_value" : str(float(line_data[9:19])/100.00),
                    "cpf" : line_data[19:30],
                    "card" : line_data[30:42],
                    "time" : f'{time_currence}',
                    "owner" : line_data[48:62].strip(),
                    "store_name" : line_data[62:80].strip(),
                }
                # print(time_currence)
                movements_data.append(transaction_data)

        for movement in movements_data:
            owner = Owner.objects.get_or_create(name=movement['owner'], cpf=movement['cpf'])
            store = Store.objects.get_or_create(name=movement['store_name'], owner=owner[0])
            movement_store = MovementStore.objects.create(
                transaction_type=movement['transaction_type'],
                date_of_currence=movement['date_of_currence'],
                transaction_value=movement['transaction_value'],
                card=movement['card'],
                time=movement['time'],
                store_name=store[0]
            )
            
            print(movement_store)
            # print(store[0])
            # print(owner[0])

        # ipdb.set_trace()


        return document