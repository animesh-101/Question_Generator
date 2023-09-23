from django.shortcuts import render

def index(request):
    return render(request, 'Generator/index.html')

def converter(request):
    return render(request, 'Generator/convert.html' )
