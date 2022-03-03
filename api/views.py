from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from table_app.models import TableData
from .serializers import DataSerializer
import django_filters
from rest_framework import filters


class DataList(generics.ListCreateAPIView):
    serializer_class = DataSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['quantity', 'distance']
    ordering_fields = ['quantity', 'distance']
    def get(self, request):
        try:
            parents = []
            parent_categories = TableData.objects.filter(parent_id=0)
            for pc in parent_categories:
                childs = []
                for child in TableData.objects.filter(parent_id=pc.id):
                    childs.append({
                        "id": child.id,
                        "date": child.date,
                        "name": child.name,
                        "quantity": child.quantity,
                        "distance": child.distance,
                    })
                parents.append({
                    "id": pc.id,
                    "date": pc.date,
                    "name": pc.name,
                    "quantity": pc.quantity,
                    "distance": pc.distance,
                    "childs": childs,
                })
            return Response(parents)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def queryset(request):


        qs = request.GET.get('qs') if request.GET.get('q') != None else ''

        product_filter = TableData.objects.filter(Q(quantity__gt=qs))

        pass
    

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TableData.objects.all()
    serializer_class = DataSerializer

