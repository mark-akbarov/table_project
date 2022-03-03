from django.shortcuts import render
from .models import TableData
from django.db.models import Q


def is_valid_param(param):
    return param is not None and param != ''


def home(request):

    qs = TableData.objects.all()

    less_than = request.GET.get('less_than')
    greater_than = request.GET.get('greater_than')
    equal_to = request.GET.get('equal_to')


    if is_valid_param(less_than):
        qs = qs.filter(quantity__gt = less_than)
 
    elif is_valid_param(greater_than):
        qs = qs.filter(quantity__lt = greater_than)
    
    elif is_valid_param(equal_to):
        qs = qs.filter(quantity__gt = equal_to)
 
    
    

    return render(request, 'table_app/home.html', {'qs': qs})