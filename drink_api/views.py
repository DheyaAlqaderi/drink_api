from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer


def drink_list(request):

    #get all data
    drink = Drink.objects.all()

    #serialize the data
    seriliazer = DrinkSerializer(drink, many=True)

    #return the json
    return JsonResponse({'drinks': seriliazer.data})


