from rest_framework import serializers

from .models import Movement

import ipdb

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
                transaction_data = {
                    "transaction_type" : line_data[0],
                    "date_of_occurrence" : line_data[1:9],
                    "transaction_value" : line_data[9:19],
                    "cpf" : line_data[19:30],
                    "card" : line_data[30:42],
                    "time" : line_data[42:48],
                    "owner" : line_data[48:62],
                    "store_name" : line_data[62:80],
                }

                movements_data.append(transaction_data)



        return document