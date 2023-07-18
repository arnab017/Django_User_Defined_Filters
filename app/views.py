from django.shortcuts import render

# Create your views here.

def user_defined_filters(request):
    d = {'data':'Hello Hai Are You',
         'data2':'This MORNING IS VERY Beautiful'}
    return render(request, 'user_defined_filters.html',d)
