from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def api_item_single(request, pk):

    try:
        article = Item.objects.get(id=pk)
        serializer = ItemSerializer(article)
        return Response(serializer.data, status=200)
    except Item.DoesNotExist:
        return Response({"error": "Article doesnt exist"}, status=404)

@api_view(['GET', 'POST'])
def api_item(request):

    if request.method == 'GET':
        try:
            article = Item.objects.get(name="test 123")
            serialized_data = ItemSerializer(article)
            return Response(serialized_data.data)
        except Item.DoesNotExist:
            return Response({
                "error": "This item doesnt exist"
            }, status=404)

    elif request.method == 'POST':
        # Uzimamo JSON podatak pretvaramo u Python objekat
        serializer = ItemSerializer(data=request.data)

        # Proveravamo da li su sva polja prosledjena (koja su definisana u modelu)
        # Proveravamo tipove podataka iz Modela
        if serializer.is_valid():
            serializer.save() # Snima u tabelu Item
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    return Response({
        'message': 'Invalid API request'
    }, status=400)