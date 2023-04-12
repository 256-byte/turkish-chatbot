from rest_framework.response import Response
from rest_framework.decorators import api_view
from turkishchatbotapp.models import Item
from .serializers import ItemSerializer
import requests

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sendRequest(request):
    url = 'https://api.publicapis.org/entries'
    return Response(requests.get(url))
    # if response.status_code == 200:
    #     data = response.json()
    #     # do something with the data
    # else:
    #     # handle the error response