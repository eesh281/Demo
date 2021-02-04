from rest_framework import serializers
from .models import List,Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):

    cards = serializers.SerializerMethodField()

    class Meta:
        model = List
        fields = '__all__'

    def get_cards(self,instance):
        card_obj = Card.objects.filter(lists=instance)
        return CardSerializer(card_obj,read_only=True, many=True).data




