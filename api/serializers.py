from table_app.models import TableData
from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TableData
        fields = ['date', 'name', 'quantity', 'distance']
