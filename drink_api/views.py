from django.http import Http404, JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        #get all data
        drink = Drink.objects.all()
        #serialize the data
        seriliazer = DrinkSerializer(drink, many=True)
        #return the json
        return Response(seriliazer.data)
    elif request.method == 'POST':
        seriliazer = DrinkSerializer(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink(request, id):

    #get all data
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        #serialize the data
        seriliazer = DrinkSerializer(drink)
        #return the json
        return JsonResponse(seriliazer.data)
    elif request.method == 'PUT':
        seriliazer =DrinkSerializer(drink, data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response(seriliazer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        