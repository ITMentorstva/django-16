from django.shortcuts import render

from .models import Item
from .serializers import ItemSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name','description','created_at']

    filterset_fields = {
        'price': ['gte', 'lte', 'exact'],
        'created_at': ['gte', 'lte', 'exact', 'date']
    }

    @action(detail=False, methods=['get'])
    def cheapest(self, request):

        article = Item.objects.order_by('price').first()
        if article:
            serializer = ItemSerializer(article)
            return Response(serializer.data)

        return Response({'error': 'There is no data at the moment'}, status=400)