# from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html')

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request,'map.html')
def services(request):
    return render(request,'services.html')
def bus(request):
    return render(request,'bus.html')
def train(request):
    return render(request,'train.html')
def flight(request):
    return render(request,'flight.html')
def register(request):
    return render(request,'register.html')