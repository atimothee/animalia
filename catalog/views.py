from django.shortcuts import render_to_response
from catalog.models import Animal

def home(request):
    return render_to_response('home.html', {})

def animal_list(request):
    animals = Animal.objects.filter(name__icontains=request.GET.get('name', ''))
    return render_to_response('catalog/catalog_list.html', {'animals': animals})
