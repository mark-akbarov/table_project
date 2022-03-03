from table_app.models import TableData
import django_filters

class UserFilter(django_filters.FilterSet):
    
    class Meta:
        model = TableData
        fields = ['name', 'quantity', 'distance', ]