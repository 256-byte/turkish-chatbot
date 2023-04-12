from rest_framework import serializers
from turkishchatbotapp.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        # fields = ['id', 'name']